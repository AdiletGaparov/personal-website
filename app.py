import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
import numpy as np
import altair as alt
import datetime as dt
import pickle
from joblib import dump, load

from textblob import TextBlob
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC, SVC
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import VotingClassifier


from utils import img_to_bytes, img_html, read_markdown_file, gantt_chart, language_chart, travel_chart, programming_language_chart
from load_data import load_history, load_language, load_courses, load_travel, load_programming_lang

# fixing random seed
np.random.seed(289)

# Contact info
linkedin = img_html('media/linkedin_logo.png', 'max-width:32px', '')
github = img_html('media/github_logo.png', 'max-width:32px', '')
facebook = img_html('media/facebook_logo.png', 'max-width:32px', '')
instagram = img_html('media/instagram_logo.png', 'max-width:32px', '')
email = img_html('media/icons8-mail.png', 'max-width:32px', '')

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


# Sidebar
st.sidebar.markdown("# Navigation")
navigation_options = ['Home', 'Projects', 'Resume']
page = st.sidebar.radio(label = '', options = navigation_options, key=0)
st.sidebar.markdown('---')

# Content
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
        st.sidebar.audio('media/name.mp3')

    # Main page
    avatar = "<img src='data:image/jpg;base64,{}' class='img-fluid rounded-circle mx-auto d-block' style='max-width:25%'>".format(
        img_to_bytes("media/avatar.jpg")
    )
    st.markdown(avatar, unsafe_allow_html=True)
    st.markdown(read_markdown_file("markdown/intro.md"), unsafe_allow_html=True)

    components.html(socia_media_links, height=40)

elif page == 'Projects':

    # Additional sidebar
    st.sidebar.markdown('### Tech Demo')

    fake_test = st.sidebar.text_input('Fake News detector')
    st.sidebar.markdown(fake_test)

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
        st.write('To be written')

        st.markdown('---' m)
    if st.button('Travel and photos "My camino"'):
        travel_history = load_travel()
        travel = travel_chart(travel_history)
        st.altair_chart(travel, use_container_width=True)

        st.markdown('---')
    if st.button('Fake News Detection'):
        nlp_wiki = f"""
        <details class="shadow p-3 mb-5 bg-white rounded">
        <summary><i>Small wiki of concepts</i></summary>
        <br/>
        <div>
            <strong>Corpus</strong>: set of <i>documents</i> (our dataset of news with <i>fake</i> and <i>real</i> labels).
        </div>
        <div>
            <strong>Documents</strong>: basic unit or object (a particular news or tweet).
        </div>
        <div>
            <strong>Bag-of-Words (BoW) representation</strong>: representation of documents as a collection words with count value for each word.
            In this representation, what is important is how many times a particular word appears in the corpus and in each document, but not the order of words. 
            There are 3 main ways to calculate <i>count value</i> for each word: <i>binary weighting</i>, <i>TF weighting</i>, and <i>TF-IDF weighting</i>
        </div>
        <div class='text-center'>
            {img_html('media/wiki-bow-repr.png', 'max-width:50%', 'img-fluid')}
        </div>
        <div>
            <strong>Binary weighting</strong>: the count value is binary indicator (does this word exist in this document?)
        </div>
        <div class='text-center'>
            {img_html('media/wiki-binary-w.png', 'max-width:50%', 'img-fluid')}
        </div>
        <div>
            <strong>Term Frequency (TF) weighting</strong>: the count value is just frequency of a word (how many times does this word appear in this document?).
        </div>
        <div class='text-center'>
            {img_html('media/wiki-tf-w.png', 'max-width:50%', 'img-fluid')}
        </div>
        <div>
            <strong>Term Frequency-Inverse Document Frequency (TF-IDF) weighting</strong>: in TF weighting the words like articles (the, a) appear a lot in each document, which bring little information to distinguish documents. 
            We want rare words, because they are more informative that frequent ones (articles, pronouns, etc). 
            We can solve this problem by taking into account the number of documents in which they appear. 
            Therefore, the count value is real-valued number that is proportional to frequency of a word in this document and inversely proportionally to frequency of documents in which this word appears.
        </div>
        <div class='text-center'>
            {img_html('media/wiki-tf-idf-w.png', 'max-width:50%', 'img-fluid')}
        </div>
        <div>
            <strong>Stopwords</strong>: common words, that bear little value for differentiation, like articles and pronouns. 
        </div>
        <div>
            <strong>Tokens and tokenization</strong>: separation of a sentence into words (<i>tokens</i>).
        </div>
        <div>
            <strong>Stems and stemming</strong>: crude chopping of affixes to base words (<i>stems</i>), so that several similar words convert to one. For example, "automate(s)", "automatic", "automation" all reduces to "automat".
        </div>
        <div>
            <strong>Lemma and lemmatization</strong>: reduction of inflections or variant forms to meaningful base form (<i>lemma</i>). For example, "are", "is", "am" become "be", while "cars" becomes "car". Lemmatizatin is more powerful than stemming, but also takes much more time.
        </div>
        <div>
            <strong>N-grams (unigrams, bigrams)</strong>: contiguous sequence of N words. One word is <i>unigram</i>, two words are called <i>bigram</i>.
        </div>
        </details>
        """

        st.markdown(read_markdown_file('markdown/fake_news_detection_overview.md'), unsafe_allow_html=True)
        st.markdown(nlp_wiki, unsafe_allow_html=True)

        st.markdown('---')
    if st.button('Sentiment-based Music Recommender'):
        st.info("**Disclaimer**: this is a group project, but the MVP web app was written by me using Flask (micro web framework written in Python), pure JavaScript, and SoundCloud API. You can find the code on my [GitHub](https://github.com/AdiletGaparov/sentiment-based-song-recommender).")
        st.markdown(read_markdown_file('markdown/sentiment_music_recommender.md'), unsafe_allow_html=True)
        st.image('media/JS-sentiment-recommender.png', use_column_width=True, format='PNG')

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

elif page == 'Chatbot':
    st.write('Chatbot')