import streamlit as st
import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import json

import os
import gdown

# Check if file already exists
if not os.path.exists("similarity.pkl"):
    # File ID from Google Drive shareable link
    file_id = "1xWUYeuK-Wquhemi5pxw4of1vwnWdWgXA"
    gdown.download(f"https://drive.google.com/uc?id={file_id}", "similarity.pkl", quiet=False)

def fetch_poster_and_rating(movie_id):
    api_key = 'your_tmdb_api_key'  # Replace this with your actual API key
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    try:
        response = requests.get(url)
        data = response.json()
        rating = data.get('vote_average', 'N/A')
        # Check if 'poster_path' exists and is not None
        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/w500" + data['poster_path'], rating
        else:
            # Fallback image if poster is missing
            return "https://imageplaceholder.net/600x400/eeeeee/131313?text=Poster+Not+Found" , rating
    except:
        # Fallback if the API call fails
        return "https://imageplaceholder.net/600x400/eeeeee/131313?text=Poster+Not+Found" , 'N/A'

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_ids = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_ids.append(movie_id)
    return recommended_movies, recommended_movie_ids

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Enter the movie',movies['title'].values)

if st.button("Recommend"):
    names, movie_ids = recommend(selected_movie_name)

    posters_and_ratings = [fetch_poster_and_rating(mid) for mid in movie_ids]

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            poster_url, rating = posters_and_ratings[idx]
            st.image(poster_url)
            st.text(names[idx])
            st.markdown(f"⭐ **Rating**: {rating}")

