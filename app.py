import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
from utils import img_to_bytes, icon_html, read_markdown_file, gantt_chart, language_chart, travel_chart, programming_language_chart
from load_data import load_history, load_language, load_courses, load_travel, load_programming_lang
import altair as alt
import datetime as dt

# Sidebar
st.sidebar.markdown("# Navigation")
navigation_options = ['Home', 'Projects', 'Resume']
page = st.sidebar.radio(label = '', options = navigation_options, key=0)
st.sidebar.markdown('---')
st.sidebar.markdown('### FAQ')
if st.sidebar.button('Not sure how to pronounce my name?'):
    st.sidebar.audio('name.mp3')

# Content
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden; padding:0}
"""

if page == 'Home':
    avatar = "<img src='data:image/jpg;base64,{}' class='img-fluid rounded-circle mx-auto d-block' style='max-width:25%'>".format(
        img_to_bytes("media/avatar.jpg")
    )
    st.markdown(avatar, unsafe_allow_html=True)
    st.markdown(read_markdown_file("markdown/intro.md"), unsafe_allow_html=True)

    linkedin = icon_html('media/linkedin_logo.png', 'max-width:32px')
    github = icon_html('media/github_logo.png', 'max-width:32px')
    facebook = icon_html('media/facebook_logo.png', 'max-width:32px')
    instagram = icon_html('media/instagram_logo.png', 'max-width:32px')
    email = icon_html('media/icons8-mail.png', 'max-width:32px')

    socia_media_links = f"""
    <div style='text-align:center;'>
        <div style='inline-block'>
        <a href='mailto:adilet.gaparov@gmail.com' style='margin-right:5px'>{email}</a>
        <a href="http://www.linkedin.com/in/adilet-gaparov" target= '_blank' style='margin:5px'>{linkedin}</a>
        <a href="http://www.github.com/adiletgaparov" target= '_blank' style='margin:5px'>{github}</a>
        <a href="http://www.facebook.com/adiletgaparov" target='_blank' style='margin:5px'>{facebook}</a>
        <a href="http://www.instagram.com/adilet.gaparov" target='_blank' style='margin:5px'>{instagram}</a>
        </div>
    </div>
    """
    components.html(socia_media_links, height=40)

    # Hide streamlit style (footer and hamburger menu)
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

elif page == 'Projects':
    st.markdown(
        """
        <div style = "text-align: center">
            <div style = "display: inline-block; max-width: 60%">
            <h3>Projects</h3><br/>
        </div></div >
        """,
        unsafe_allow_html=True
    )

    if st.button('How I built this website'):
        st.write('To be written')
    if st.button('Travel and photos "My camino"'):
        travel_history = load_travel()
        travel = travel_chart(travel_history)
        st.altair_chart(travel, use_container_width=True)
    if st.button('Fake News Detection'):
        st.write('A bit of description/intro/dataset and demo: https://github.com/AdiletGaparov/mbd-natural-language-processing/tree/master/fake-news-detection')
    if st.button('Sentiment-based Music Recommender'):
        st.write('Would be cool to have it, but challenging to implement inside app here: https://github.com/AdiletGaparov/sentiment-based-song-recommender')

    # Hide streamlit style (footer and hamburger menu)
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

elif page == 'Resume':
    # Experience section
    experience_subtitle = '''
        <div style="text-align: center"><div style="display: inline-block; max-width: 60%"> 
        <h3>Experience</h3>
        <br/>
        </div></div>
        '''
    life_history = load_history()
    st.markdown(experience_subtitle, unsafe_allow_html=True)

    gantt = gantt_chart(life_history.query("org != 'Key moments'"))
    scatter = alt.Chart(life_history.query("org == 'Key moments'")).mark_circle().encode(
        x=alt.X('start:T', axis=alt.Axis(title='', orient='top', format='%b %Y')),
        y=alt.Y('org:N', sort=None, axis=alt.Axis(title='')),
        tooltip=['location', 'description'],
        color=alt.Color('color', scale=None)
    ).interactive()
    resume_chart = alt.layer(gantt, scatter).configure_view(strokeWidth=0.5)
    st.altair_chart(resume_chart, use_container_width=True)

    st.markdown('---')
    # Skills section
    skills_subtitle = '''
        <div style="text-align: center"><div style="display: inline-block; max-width: 60%"> 
        <h3>Skills</h3>
        <br/>
        </div></div>
        '''
    st.markdown(skills_subtitle, unsafe_allow_html=True)

    languages = load_language()
    lang_chart = language_chart(languages)
    programming_lang = load_programming_lang()
    programming_lang_chart = programming_language_chart(programming_lang)
    st.altair_chart(lang_chart, use_container_width=True)
    st.altair_chart(programming_lang_chart, use_container_width=True)
    st.markdown('---')

    # Courses section
    courses_subtitle = '''
            <div style="text-align: center"><div style="display: inline-block; max-width: 60%"> 
            <h3>Courses</h3>
            </div></div>
        '''
    st.markdown(courses_subtitle, unsafe_allow_html=True)

    courses = load_courses()
    courses_columns = ['Course', 'Organization', 'Status']
    chosen_topic = st.multiselect('Topic',  list(courses.Topic.unique()), list(courses.Topic.unique()))
    if not chosen_topic:
        st.write('')
    else:
        table = st.empty()
        add_columns = st.multiselect('Additional information', ['Certificate', 'Platform', 'Date', 'Topic'])
        courses_columns = courses_columns + add_columns
        table.dataframe(courses.loc[courses.Topic.isin(chosen_topic), courses_columns])

    # Hide streamlit style (footer and hamburger menu)
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

elif page == 'Chatbot':
    st.write('Chatbot')