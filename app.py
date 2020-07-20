import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
from utils import img_to_bytes, read_markdown_file, gantt_chart, language_chart, travel_chart
from load_data import load_history, load_language, load_courses, load_travel
import altair as alt
import datetime as dt

st.sidebar.markdown("# Navigation")
navigation_options = ['Home', 'Projects', 'Resume', 'Chatbot']
page = st.sidebar.radio(label = '', options = navigation_options, key=0)
st.sidebar.markdown('---')
st.sidebar.markdown('### FAQ')
if st.sidebar.button('Not sure how to pronounce my name?'):
    st.sidebar.audio('name.mp3')

if page == 'Home':
    avatar = "<img src='data:image/jpg;base64,{}' class='img-fluid rounded-circle mx-auto d-block' style='max-width:25%'>".format(
        img_to_bytes("media/avatar.jpg")
    )
    st.markdown(avatar, unsafe_allow_html=True)

    intro_markdown = read_markdown_file('markdown/intro.md')
    st.markdown(intro_markdown, unsafe_allow_html=True)

    linkedin = "<img src='data:image/png;base64,{}' style='max-width:32px'>".format(
        img_to_bytes("media/linkedin_logo.png")
    )
    github = "<img src='data:image/png;base64,{}' style='max-width:32px'>".format(
        img_to_bytes("media/github_logo.png")
    )
    facebook = "<img src='data:image/png;base64,{}' style='max-width:32px'>".format(
        img_to_bytes("media/facebook_logo.png")
    )
    instagram = "<img src='data:image/png;base64,{}' style='max-width:32px'>".format(
        img_to_bytes("media/instagram_logo.png")
    )
    email = "<img src='data:image/png;base64,{}' style='max-width:32px'>".format(
        img_to_bytes("media/icons8-mail.png")
    )

    socia_media_links = f"""
    <div style='text-align:center'>
        <div style='inline-block'>
        <a href='mailto:adilet.gaparov@gmail.com' style='margin-right:5px'>{email}</a>
        <a href="http://www.linkedin.com/in/adilet-gaparov" target= '_blank' style='margin:5px'>{linkedin}</a>
        <a href="http://www.github.com/adiletgaparov" target= '_blank' style='margin:5px'>{github}</a>
        <a href="http://www.facebook.com/adiletgaparov" target='_blank' style='margin:5px'>{facebook}</a>
        <a href="http://www.instagram.com/adilet.gaparov" target='_blank' style='margin:5px'>{instagram}</a>
        </div>
    </div>
    """
    components.html(socia_media_links)

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

elif page == 'Resume':
    resume_subtitle = '''
        <div style="text-align: center"><div style="display: inline-block; max-width: 60%"> 
        <h3>Experience</h3>
        <br/>
        </div></div>
        '''
    life_history = load_history()
    st.markdown(resume_subtitle, unsafe_allow_html=True)
    gantt = gantt_chart(life_history.query("org != 'Key moments'"))
    scatter = alt.Chart(life_history.query("org == 'Key moments'")).mark_circle().encode(
        x=alt.X('start:T', axis=alt.Axis(title='', orient='top', format='%b %Y')),
        y=alt.Y('org:N', sort=None, axis=alt.Axis(title='')),
        tooltip=['location', 'description'],
        color=alt.Color('color', scale=None)
    ).interactive()
    resume_chart = alt.layer(gantt, scatter).configure_view(strokeWidth=0.5)
    st.altair_chart(resume_chart, use_container_width=True)
    st.markdown(read_markdown_file('markdown/resume.md'), unsafe_allow_html=True)
    st.markdown('---')

    # Skills section
    skills_subtitle = '''
        <div style="text-align: center" ><div style="display: inline-block; max-width: 60%"> 
        <h3>Skills</h3>
        <br/>
        </div></div>
        '''
    st.markdown(skills_subtitle, unsafe_allow_html=True)

    languages = load_language()
    lang_chart = language_chart(languages)
    st.altair_chart(lang_chart)
    st.markdown('---')

    # Courses section
    courses_subtitle = '''
            <div style="text-align: center" ><div style="display: inline-block; max-width: 60%"> 
            <h3>Courses</h3>
            </div></div>
        '''
    st.markdown(courses_subtitle, unsafe_allow_html=True)

    courses = load_courses()
    courses_columns = ['Course', 'Organization']
    chosen_topic = st.multiselect('Topic',  list(courses.Topic.unique()), list(courses.Topic.unique()))
    if not chosen_topic:
        st.write('')
    else:
        table = st.empty()
        add_columns = st.multiselect('Add info', ['Certificate', 'Platform', 'Exact Date', 'Topic'])
        courses_columns = courses_columns + add_columns
        table.dataframe(courses.loc[courses.Topic.isin(chosen_topic), courses_columns])

elif page == 'Chatbot':
    st.write('Chatbot')