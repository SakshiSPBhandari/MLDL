import streamlit as st
import numpy as np
import pickle

# st.set_page_config(layout='wide')

df = pickle.load(open("df_new.pkl", 'rb'));
similarity = pickle.load(open("similarity.pkl", 'rb'));


def recommend(drama):
    drama_index = df[df['Title'] == drama].index[0]
    distances = sorted(list(enumerate(similarity[drama_index])), reverse=True, key=lambda x: x[1])[1:7]
    recommended_title = []
    recommended_story = []
    for i in distances[1:7]:
        recommended_title.append(df.iloc[i[0]].Title)
        if df.iloc[i[0]].Story == "add a plot":
            recommended_story.append("Story Not Available")
        else:
            recommended_story.append(df.iloc[i[0]].Story)

    return recommended_title, recommended_story

st.markdown("""
<style>
.big-font {
    font-size:38px !important;
    text-transform:capitalize;
    font-weight:bold;
    text-align:center;
}
.styling{
    font-style: bold;
    text-decoration: underline;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Select the Kdrama From Below</p>', unsafe_allow_html=True)

name = st.selectbox("", df['Title'])

if st.button('Recommend'):
    title, story = recommend(name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with st.container():
        new_title = '<p class="styling" style="font-family:sans-serif; color:#341641; font-size: 22px; text-transform: capitalize;">' + \
                    story[0] + '</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown(story[0], unsafe_allow_html=True)

    with st.container():
        new_title = '<p class="styling" style="font-family:sans-serif; color:#341641; font-size: 22px;text-transform: capitalize;">' + \
                    title[1] + '</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown(story[1], unsafe_allow_html=True)

    with st.container():
        new_title = '<p class="styling" style="font-family:sans-serif; color:#341641; font-size: 22px;text-transform: capitalize;">' + \
                    title[2] + '</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown(story[2], unsafe_allow_html=True)

    with st.container():
        new_title = '<p class="styling" style="font-family:sans-serif; color:#341641; font-size: 22px;text-transform: capitalize;">' + \
                    title[3] + '</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown(story[3], unsafe_allow_html=True)

    with st.container():
        new_title = '<p class="styling" style="font-family:sans-serif; color:#341641; font-size: 22px;text-transform: capitalize;">' + \
                    title[4] + '</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown(story[4], unsafe_allow_html=True)
