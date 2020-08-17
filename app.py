import streamlit as st
import streamlit.components.v1 as components
import altair as alt

# Header
st.beta_set_page_config(
    page_title='Adilet Gaparov | personal website',
    page_icon='media/avatar.jpg',
    layout='wide',
    initial_sidebar_state='auto'
)

from textblob import TextBlob

from utils import img_to_bytes, read_markdown_file, gantt_chart, language_chart, coding_language_chart

# import resume content
from content.contact_info import socia_media_links
from content.resume import history, languages, courses, coding

# import project content
from content.this_website_pm.project_wikihow_wireframes import wireframes
from content.fake_news.project_fake_news_p2 import project_fake_news_p2
from content.fake_news.project_fake_news_p5 import project_fake_news_p5
from content.fake_news.project_fake_news_glossary import nlp_glossary
project_fake_news_info = read_markdown_file('content/fake_news/project_fake_news_info.md')
project_fake_news_p1 = read_markdown_file('content/fake_news/project_fake_news_p1.md')
project_fake_news_p3 = read_markdown_file('content/fake_news/project_fake_news_p3.md')
project_fake_news_p4 = read_markdown_file('content/fake_news/project_fake_news_p4.md')
project_fake_news_p6 = read_markdown_file('content/fake_news/project_fake_news_p6.md')
project_wikihow_engineering = read_markdown_file('content/this_website_pm/project_wikihow_engineering.md')
project_wikihow_backlog = read_markdown_file('content/this_website_pm/backlog.html')
project_wikihow_prd = read_markdown_file('content/this_website_pm/PRD.html')
project_wikihow_design = read_markdown_file('content/this_website_pm/project_wikihow_design.md')
project_music_recommender = read_markdown_file('content/music_recommender/project_music_recommender.md')
project_music_recommender_info = read_markdown_file('content/music_recommender/project_music_recommender_info.md')

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
    st.write(avatar, unsafe_allow_html=True)
    st.write(read_markdown_file("content/intro.md"), unsafe_allow_html=True)

    components.html(socia_media_links, height=40)

elif page == 'Projects':

    # Additional sidebar
    st.sidebar.markdown('### Tech Demo')

    sentiment_test = TextBlob(st.sidebar.text_input('Sentiment Polarity & Subjectivity'))
    if sentiment_test:
        st.sidebar.markdown(f"""
            Polarity: {round(sentiment_test.sentiment.polarity,2)}   
            Subjectivity: {round(sentiment_test.sentiment.subjectivity,2)}
        """)
    st.sidebar.markdown('---')
    feedback = st.sidebar.text_input('Feedback')
    if feedback:
        st.sidebar.markdown(f'Your feedback: {feedback}')
        st.sidebar.warning("""
                    Hi, thanks for giving feedback! I appreciate it! 
                    As you will see in the backlog under "How I built this website", I have not implemented this feature yet.
                    However, feedback is a gift. Please, share it with me again directly 👇. 
                    """)
        st.sidebar.markdown(socia_media_links, unsafe_allow_html=True)

    # Main page
    st.write(
        """
        <div style = "text-align: center">
            <div style = "display: inline-block; max-width: 60%">
            <h3>Projects</h3><br/>
        </div></div >
        """,
        unsafe_allow_html=True
    )

    if st.checkbox('How I built this website'):

        st.write('---')
        st.write('**Product Requirement Document**')
        components.html(project_wikihow_prd, height=550, scrolling=True)
        st.write('---')
        st.write(project_wikihow_design, unsafe_allow_html=True)
        st.write('---')
        st.write('**Design - Wireframes ([Balsamiq Wireframes](https://balsamiq.com/))**')
        components.html(wireframes, height=550, scrolling=True)
        st.write('---')
        st.write(project_wikihow_engineering)
        st.write('---')
        st.write('**Backlog**')
        components.html(project_wikihow_backlog, height=300, scrolling=True)
        st.write('---')

    if st.checkbox('Fake News Detection'):

        st.info(project_fake_news_info)
        st.write(project_fake_news_p1, unsafe_allow_html=True)
        st.write(project_fake_news_p2, unsafe_allow_html=True)
        st.write(project_fake_news_p3, unsafe_allow_html=True)
        st.write(project_fake_news_p4, unsafe_allow_html=True)
        st.write(project_fake_news_p5, unsafe_allow_html=True)
        st.write(project_fake_news_p6, unsafe_allow_html=True)
        st.write(nlp_glossary, unsafe_allow_html=True)

        st.write('---')

    if st.checkbox('Sentiment-based Music Recommender'):

        st.info(project_music_recommender_info)
        st.write(project_music_recommender, unsafe_allow_html=True)
        st.image('media/project-music-recommender-ui.png', use_column_width=True, output_format='PNG')


        st.write('---')

elif page == 'Resume':

    # Additional sidebar
    st.sidebar.info('Tip: hover over or click on charts to get more information')
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
    history_df = history()
    st.write(experience_subtitle, unsafe_allow_html=True)

    gantt = gantt_chart(history_df.query("org != 'Key moments'"))
    scatter = alt.Chart(history_df.query("org == 'Key moments'")).mark_circle().encode(
        x=alt.X('start:T', axis=alt.Axis(title='', orient='top', format='%b %Y')),
        y=alt.Y('org:N', sort=None, axis=alt.Axis(title='')),
        tooltip=['location', 'description'],
        color=alt.Color('color', scale=None)
    ).interactive()
    resume_chart = alt.layer(gantt, scatter).configure_view(strokeWidth=0.5).properties(width=660)
    st.altair_chart(resume_chart, use_container_width=True)

    st.write('---')

    # Skills section
    skills_subtitle = '''
        <div style="text-align: center"><div style="display: inline-block; max-width: 60%"> 
        <h3>Skills</h3>
        <br/>
        </div></div>
        '''
    st.write(skills_subtitle, unsafe_allow_html=True)

    lang_chart = language_chart(languages())
    coding_chart = coding_language_chart(coding())
    st.altair_chart(lang_chart, use_container_width=True)
    st.altair_chart(coding_chart, use_container_width=True)
    st.write('---')

    # Courses section
    courses_subtitle = '''
            <div style="text-align: center"><div style="display: inline-block; max-width: 60%"> 
            <h3>Courses</h3>
            </div></div>
        '''
    st.write(courses_subtitle, unsafe_allow_html=True)

    courses_df = courses()
    courses_columns = ['Course', 'Organization', 'Status']
    chosen_topic = st.multiselect('Topic',  list(courses_df.Topic.unique()), list(courses_df.Topic.unique()))
    if not chosen_topic:
        st.write('')
    else:
        table = st.empty()
        add_columns = st.multiselect('Additional information', ['Certificate', 'Platform', 'Date', 'Topic'])
        courses_columns = courses_columns + add_columns
        table.dataframe(courses_df.loc[courses_df.Topic.isin(chosen_topic), courses_columns])

elif page == 'Chatbot':
    st.write('Chatbot')