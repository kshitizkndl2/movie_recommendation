import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies['title'][i[0]])
    return recommended_movies
    for i in movies_list:
        print(new_df['title'][i[0]])

movies_list = pickle.load(open('movies_list.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommender System")

option = st.selectbox("Select a movie",movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)
