import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss
from flask import Flask, request, jsonify, render_template

# Load the MovieLens dataset
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Preprocess movie genres
movies['genres'] = movies['genres'].fillna('')

# TF-IDF Vectorization for Content-Based Filtering
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = vectorizer.fit_transform(movies['genres'])

# Convert TF-IDF matrix to dense format for Faiss
tfidf_dense = tfidf_matrix.toarray().astype('float32')

# Hybrid cosine similarity
index = faiss.IndexFlatL2(tfidf_dense.shape[1])
index.add(tfidf_dense)

# Flask app
app = Flask(__name__)

def get_top_k_similar_movies(movie_index, k=10):
    """Retrieve top-k similar movies for a given movie index using Faiss."""
    distances, indices = index.search(tfidf_dense[movie_index].reshape(1, -1), k)
    return indices.flatten()

@app.route('/')
def home():
    """Serve the navigation page."""
    return render_template('home.html')

@app.route('/ratings')
def ratings_page():
    """Serve the recommendations based on ratings page."""
    return render_template('ratings.html')

@app.route('/preferences')
def preferences_page():
    """Serve the recommendations based on preferences page."""
    return render_template('preferences.html')

@app.route('/recommend-ratings', methods=['POST'])
def recommend_ratings():
    """API to recommend movies based on User Ratings."""
    user_id = request.json.get('userId')
    
    # Get the movies rated by the user
    user_ratings = ratings[ratings['userId'] == int(user_id)]
    if user_ratings.empty:
        return jsonify({"error": "User not found"}), 404

    # Pick the highest-rated movie by the user
    favorite_movie_id = user_ratings.sort_values(by='rating', ascending=False).iloc[0]['movieId']
    movie_index = movies[movies['movieId'] == favorite_movie_id].index[0]

    # Get similar movies using Faiss
    similar_movies_indices = get_top_k_similar_movies(movie_index, k=10)

    # Retrieve movie details
    recommendations = movies.iloc[similar_movies_indices].to_dict(orient='records')
    return jsonify(recommendations)

@app.route('/recommend-preferences', methods=['POST'])
def recommend_preferences():
    """API to recommend movies based on User Preferences (Favorite Movies and Genres)."""
    favorite_movies = request.json.get('favoriteMovies', [])
    favorite_genres = request.json.get('favoriteGenres', [])
    
    recommended_movies = []

    if favorite_movies:
        for movie_title in favorite_movies:
            movie_index = movies[movies['title'].str.contains(movie_title.strip(), case=False, na=False)]
            if not movie_index.empty:
                movie_index = movie_index.index[0]
                similar_movies = get_top_k_similar_movies(movie_index, k=10)
                recommended_movies.extend(movies.iloc[similar_movies].to_dict(orient='records'))
        
        # Remove duplicate recommendations by movieId
        recommended_movies = list({v['movieId']: v for v in recommended_movies}.values())[:10]

    elif favorite_genres:
        recommended_movies = movies[movies['genres'].str.contains('|'.join(favorite_genres), case=False)]
        if recommended_movies.empty:
            return jsonify({"error": "No movies found for the selected genres"}), 404
        recommended_movies = recommended_movies.head(10).to_dict(orient='records')
    
    else:
        return jsonify({"error": "No preferences provided"}), 400
    
    return jsonify(recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
