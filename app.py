import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

import altair as alt

from textblob import TextBlob

from utils import img_to_bytes, read_markdown_file, gantt_chart, language_chart, coding_language_chart
from load_data import load_history, load_language, load_courses, load_coding_lang

# import content
from content.contact_info import socia_media_links
from content.project_wikihow_wireframes import wireframes
from content.project_fake_news_p2 import project_fake_news_p2
from content.project_fake_news_p5 import project_fake_news_p5
from content.project_fake_news_glossary import nlp_glossary
project_fake_news_p1 = read_markdown_file('content/project_fake_news_p1.md')
project_fake_news_p3 = read_markdown_file('content/project_fake_news_p3.md')
project_fake_news_p4 = read_markdown_file('content/project_fake_news_p4.md')
project_fake_news_p6 = read_markdown_file('content/project_fake_news_p6.md')
project_wikihow_engineering = read_markdown_file('content/project_wikihow_engineering.md')

# Sidebar
st.sidebar.markdown("# Navigation")
navigation_options = ['Home', 'Projects', 'Resume']
page = st.sidebar.radio(label = '', options = navigation_options, key=0)
st.sidebar.markdown('---')

# Main
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden; padding:0}
"""
# Hide streamlit style (footer and hamburger menu)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if page == 'Home':

    # Additional sidebar
    st.sidebar.markdown('### FAQ')
    if st.sidebar.button('Not sure how to pronounce my name?'):
        st.sidebar.audio('media/sound-name.mp3')

    # Main page
    avatar = "<img src='data:image/jpg;base64,{}' class='img-fluid rounded-circle mx-auto d-block' style='max-width:25%'>".format(
        img_to_bytes("media/avatar.jpg")
    )
    st.markdown(avatar, unsafe_allow_html=True)
    st.markdown(read_markdown_file("content/intro.md"), unsafe_allow_html=True)

    components.html(socia_media_links, height=40)

elif page == 'Projects':

    # Additional sidebar
    st.sidebar.markdown('### Tech Demo')

    # BACKLOG
    #fake_test = st.sidebar.text_input('Fake News detector')
    #st.sidebar.markdown(fake_test)

    sentiment_test = TextBlob(st.sidebar.text_input('Sentiment Polarity & Subjectivity'))
    if sentiment_test:
        st.sidebar.markdown(f"""
            Polarity: {round(sentiment_test.sentiment.polarity,2)}   
            Subjectivity: {round(sentiment_test.sentiment.subjectivity,2)}
        """)

    # Main page
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
        st.markdown('---')
        st.markdown('**Product Requirement Document**')
        components.html(read_markdown_file('content/PRD.html'), height=500, scrolling=True)
        st.markdown('---')
        st.markdown('**Design**')
        st.markdown("""
        1. Why design is like analytical dashboard?    
        2. What are other design justifications (color, text, format, etc)? 
        """)
        st.markdown('---')
        st.write('**Design - Wireframes ([Balsamiq Wireframes](https://balsamiq.com/))**')
        components.html(wireframes, height=550, scrolling=True)
        st.markdown('---')
        st.markdown(project_wikihow_engineering)
        st.markdown('---')
        st.markdown('**Feedback**')
        st.text_input('')
        st.markdown('---')
        st.write('**Backlog**')
        components.html(read_markdown_file('content/backlog.html'), height=300, scrolling=True)
        st.markdown('---')


    # BACKLOG
    #if st.button('Travel and photos "My camino"'):
    #    travel_history = load_travel()
    #    travel = travel_chart(travel_history)
    #    st.altair_chart(travel, use_container_width=True)
    #    st.markdown('---')

    if st.button('Fake News Detection'):

        st.info("""
            **Disclaimer**: feel free to check *Glossary of NLP concepts* below. 
            Words explained in the glossary are _italic_. 
            Besides, you can find my Jupyter Notebook with the dataset and full description on my [GitHub](https://github.com/AdiletGaparov/mbd-natural-language-processing/tree/master/fake-news-detection). 
        """)

        st.markdown(project_fake_news_p1, unsafe_allow_html=True)
        st.markdown(project_fake_news_p2, unsafe_allow_html=True)
        st.markdown(project_fake_news_p3, unsafe_allow_html=True)
        st.markdown(project_fake_news_p4, unsafe_allow_html=True)
        st.markdown(project_fake_news_p5, unsafe_allow_html=True)
        st.markdown(project_fake_news_p6, unsafe_allow_html=True)
        st.markdown(nlp_glossary, unsafe_allow_html=True)

        st.markdown('---')
    if st.button('Sentiment-based Music Recommender'):
        st.info("""
            **Disclaimer**: this is a group project, but the MVP web app was written by me using Flask (micro web framework written in Python), pure JavaScript, and SoundCloud API.
            You can find the code on my [GitHub](https://github.com/AdiletGaparov/sentiment-based-song-recommender). 
            You can test TextBlob library on the navigation panel under Tech Demo (left)."""
        )
        st.markdown(read_markdown_file('content/project_music_recommender.md'), unsafe_allow_html=True)
        st.image('media/project-music-recommender-ui.png', use_column_width=True, format='PNG')

        st.markdown('---')

elif page == 'Resume':

    # Additional sidebar
    if st.sidebar.button('Contact me'):
        st.sidebar.markdown(socia_media_links, unsafe_allow_html=True)

    # Main page
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
    coding_lang = load_coding_lang()
    coding_lang_chart = coding_language_chart(coding_lang)
    st.altair_chart(lang_chart, use_container_width=True)
    st.altair_chart(coding_lang_chart, use_container_width=True)
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

elif page == 'Chatbot':
    st.write('Chatbot')