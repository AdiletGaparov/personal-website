import numpy as np
import pandas as pd

def present_subj(option):
    subject_list_dict = {'subjective-20': '0-20% / Python, R, SQL',
                         'subjective-40': '20-40% / Hadoop, Spark, Streaming',
                         'subjective-60': '40-60% /Machine Learning',
                         'subjective-80': '60-80% / Data Visualization',
                         'subjective-100': '80-100% / Ethics, Agile, Design Thinking',
                         'all': 'All'}

    return subject_list_dict[option]


def present_polarity(option):
    level_list_dict = {'very-low': 'very low / I am ready',
                       'low': 'low / Need to recap few concepts',
                       'average': 'average / I still have few more days',
                       'high': 'high / Proficiency is a good grade',
                       'very-high': 'very high / God bless Gaussian curve at IE',
                       'all': 'All'}

    return level_list_dict[option]


def get_polarity_threshold(polarity_scores, level):
    if level == 'very-low':
        t_max = np.percentile(polarity_scores, 20)
        t_min = np.percentile(polarity_scores, 0)
    elif level == 'low':
        t_max = np.percentile(polarity_scores, 40)
        t_min = np.percentile(polarity_scores, 20)
    elif level == 'average':
        t_max = np.percentile(polarity_scores, 60)
        t_min = np.percentile(polarity_scores, 40)
    elif level == 'high':
        t_max = np.percentile(polarity_scores, 80)
        t_min = np.percentile(polarity_scores, 60)
    elif level == 'very-high':
        t_max = np.percentile(polarity_scores, 100)
        t_min = np.percentile(polarity_scores, 80)
    else:
        t_max = np.percentile(polarity_scores, 100)
        t_min = np.percentile(polarity_scores, 0)

    return np.round(t_min, 4), np.round(t_max, 4)


def get_filter(df, subject, genre):
    if genre == 'All':
        genre_list = df.genre.unique()
    else:
        genre_list = [genre]

    if subject == 'subjective-20':
        filter_array = (df['subjectivity_avg'] <= 0.2) & (df['genre'].isin(genre_list))
    elif subject == 'subjective-40':
        filter_array = (df['subjectivity_avg'] > 0.2) & (df['subjectivity_avg'] <= 0.4) & (
            df['genre'].isin(genre_list))
    elif subject == 'subjective-60':
        filter_array = (df['subjectivity_avg'] > 0.4) & (df['subjectivity_avg'] <= 0.6) & (
            df['genre'].isin(genre_list))
    elif subject == 'subjective-80':
        filter_array = (df['subjectivity_avg'] > 0.6) & (df['subjectivity_avg'] <= 0.8) & (
            df['genre'].isin(genre_list))
    elif subject == 'subjective-100':
        filter_array = (df['subjectivity_avg'] > 0.6) & (df['subjectivity_avg'] <= 0.8) & (
            df['genre'].isin(genre_list))
    else:
        filter_array = df['genre'].isin(genre_list)

    return filter_array