import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_p(mvi_id):
    res = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=79b0463688fdde0468f3b7972d1849d2'.format(mvi_id))
    data = res.json()
    return 'https://image.tmdb.org/t/p/w500/'+ data['poster_path']


def recomender(mvi):
    mi = movies[movies['title'] == mvi].index[0]
    d = m[mi]
    ml = sorted(list(enumerate(d)), reverse=True, key=lambda x: x[1])[1:6]
    ans = []
    pst = []
    for i in ml:
        m_id = movies.iloc[i[0]].id
        ans.append(movies.iloc[i[0]].title)
        pst.append(fetch_p( m_id))
    return ans,pst


movie_d = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_d)

m = pickle.load(open('similarities.pkl', 'rb'))



st.title('movie :blue[recomender] :sunglasses:')
option = st.selectbox(
    'How would you like to be contacted?',
    (movies['title'].values))


if st.button('click'):
    s,p = recomender(option)
    col1, col2, col3 , col4 , col5 = st.columns(5)

    with col1:
        st.text(s[0])
        st.image(p[0])

    with col2:
        st. text(s[1])
        st.image(p[1])

    with col3:
        st.text(s[2])
        st.image(p[2])
    with col4:
        st.text(s[3])
        st.image(p[3])
    with col5:
        st.text(s[4])
        st.image(p[4])
