
```markdown
Movie Recommender System

A Flask-based web application that provides movie recommendations based on user ratings and preferences. This project leverages content-based filtering (using TF-IDF and Faiss for similarity search) and user input to deliver tailored recommendations.

---

 Features

1. Content-Based Recommendations:
   - Recommends similar movies based on genres and features using TF-IDF vectorization and Faiss.

2. User Ratings-Based Recommendations:
   - Suggests movies by analyzing user-provided ratings.

3. Preferences-Based Recommendations:
   - Generates movie suggestions based on user-inputted favorite movies and genres.

4. Interactive Web Interface:
   - Navigate between different recommendation modes via a user-friendly web interface.

---

 Tech Stack

- Backend: Flask
- Machine Learning: TF-IDF (Scikit-learn), Faiss (Facebook AI Similarity Search)
- Frontend: HTML, CSS, JavaScript
- Data: MovieLens Dataset (movies.csv, ratings.csv)

---

 Installation

Prerequisites
- Python 3.8+
- Flask
- Scikit-learn
- Faiss
- Pandas

 Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/LARRYDMO
Movie-Recommendation-System
   cd Movie-Recommendation-System
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place the MovieLens dataset (`movies.csv` and `ratings.csv`) in the project directory.

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

 File Structure

```
movie-recommender/
│
├── app.py               # Main Flask application
├── templates/
│   ├── home.html        # Home page
│   ├── ratings.html     # Ratings-based recommendations page
│   ├── preferences.html # Preferences-based recommendations page
│
├── static/
│   ├── css/             # CSS files (if needed)
│   ├── js/              # JavaScript files (if needed)
│
├── movies.csv           # MovieLens movies dataset
├── ratings.csv          # MovieLens ratings dataset
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

---

## Usage

 Home Page
- Visit the home page to explore available recommendation methods.

 Recommendations Based on Ratings
1. Navigate to `/ratings`.
2. Enter your **user ID**.
3. Get movie recommendations based on your past ratings.

 Recommendations Based on Preferences
1. Navigate to `/preferences`.
2. Enter your **favorite movies** and/or **favorite genres**.
3. Get movie suggestions tailored to your preferences.

---

 Example Outputs

 Ratings-Based Recommendations
- Input: User ID = `1`
- Output: Top 10 movie recommendations based on user ratings.

 Preferences-Based Recommendations
- Input: Favorite Movies = `The Matrix`, Favorite Genres = `Action`
- Output: Top 10 movies matching the given preferences.

---

 Future Enhancements
1. Integrate hybrid recommendation approaches combining content and collaborative filtering.
2. Improve user interface for better interactivity.
3. Add support for multilingual recommendations.

---

 License
This project is licensed under the [MIT License](LICENSE).

---

 Acknowledgments
- [MovieLens Dataset](https://grouplens.org/datasets/movielens/latest/)
- Libraries: Flask, Faiss, Scikit-learn, Pandas
```

Notes:
1. Replace `your-username` with your GitHub username in the `git clone` command.
2. Include a `requirements.txt` file with the required Python packages:
   ```plaintext
   Flask
   pandas
   scikit-learn
   faiss-cpu
   ```


