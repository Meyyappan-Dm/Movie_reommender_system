# 🎬 Movie Recommender System

This is a content-based movie recommender system built with **Streamlit**. It suggests movies similar to the one selected by the user, based on metadata such as genres, cast, crew, and keywords.

## 🚀 Features

- 🔍 Search for any movie from the dataset
- 🎥 Get top 5 recommended movies
- 🖼️ View posters fetched from TMDB API
- ⭐ View movie ratings
- 🌐 Deployed with Streamlit Cloud

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- TMDB API
- GDown (to handle large file downloads)

## 📂 Files in This Repository

| File / Folder          |         Purpose                          |
|------------------------|------------------------------------------|
| `app.py`               | Main Streamlit app                       |
| `movies_dict.pkl`      | Preprocessed movie metadata              |
| `requirements.txt`     | Python dependencies                      |


> Note: The `similarity.pkl` file is too large for GitHub and is downloaded at runtime using `gdown`.

## 🔧 How It Works

1. User selects a movie from the dropdown.
2. The system finds the top 5 most similar movies using a precomputed similarity matrix.
3. For each recommendation:
   - It fetches the poster and rating from TMDB.
   - Displays them in a neat grid layout.



