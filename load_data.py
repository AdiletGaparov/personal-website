import pandas as pd
import streamlit as st
from utils import date_axis

colors = pd.DataFrame([
    {
        'category': 'Education',
        'color': '#09ab3b', # green - renewal, youth
    },
    {
        'category': 'Full-time job',
        'color': '#0068c9', # blue - tech, stability
    },
    {
        'category': 'Contract',
        'color': '#f63366', #
    },
    {
        'category': 'Business trip',
        'color': '#0068c9', # blue - related to job
    },
    {
        'category': 'Tourism',
        'color': '#ff2b2b' # red - energy, passion
    },
    {
        'category': 'Personal',
        'color': '#fffd80', # yellow - joy, happiness
    }
])

@st.cache
def load_history():
    data = pd.DataFrame([
        {
            "role": "Student - Foundation program",
            "start": date_axis(2011, 8, 9),
            "end": date_axis(2012, 6, 15),
            'category': 'Education',
            'org': 'Nazarbayev University',
            'location': 'Astana (Kazakhstan)',
            'description': """
                          • Foundation Program designed by UCL (London, UK). 
                          • 1 of 5 students to pass Advanced Math exam. 
                          • Grades: Physics (72%), Math (88%). 
            """
         },
        {
            "role": "Student - Bachelor's degree in Robotics & Mechatronics",
            "start": date_axis(2012, 8, 16),
            "end": date_axis(2016, 5, 13),
            'category': 'Education',
            'org': 'Nazarbayev University',
            'location': 'Astana (Kazakhstan)',
            'description': """
                            • GPA: 3.47/4.0. 
                            • Coordinated Kazakh-French Cultural Center (Aug 2015-May 2016) during the first year without sponsorship, organized the first paid French classes for students.
            """
         },
        {
            "role": "Student - French",
            "start": date_axis(2014, 6, 1),
            "end": date_axis(2014, 7, 31),
            'category': 'Education',
            'org': 'Alliance française',
            'location': 'Toulouse (France)',
            'description': '• Intensive French classes to improve my accent.'
         },
        {
            "role": "Student - Exchange",
            "start": date_axis(2015, 6, 10),
            "end": date_axis(2015, 8, 10),
            'category': 'Education',
            'org': 'UW-Madison',
            'location': 'Madison, WI (USA)',
            'description': """
                            • Visiting International Student Program (VISP).
                            • Full scholarship.
                            • GPA: 4.0/4.0.
                            • Took Entrepreneurial Management and Geology.
            """
         },
        {
            "role": "Account Technology Strategist",
            "start": date_axis(2016, 5, 23),
            "end": date_axis(2016, 10, 16),
            'category': 'Full-time job',
            'org': 'Microsoft',
            'location': 'Kazakhstan',
            'description': """
                            • Served as technology adviser for 40+ enterprise customers in Kazakhstan.
                            • Generated $1.5M+ in sales opportunities of strategic products, incl. the first Internet of Things (IoT) project for local office.
            """
         },
        {
            "role": "Technology Solutions Professional",
            "start": date_axis(2016, 10, 17),
            "end": date_axis(2018, 9, 10),
            'category': 'Full-time job',
            'org': "Microsoft",
            'location': 'CIS region',
            'description': """
                            • Being in 6-person team of product specialists, responsible for driving customer technical decision towards Office 365 and Windows 10 in 9 countries.
                            • Promoted in May 2018 for leadership and teamwork skills.
            """
         },
        {
            "role": "BI Developer",
            "start": date_axis(2018, 11, 5),
            "end": date_axis(2019, 3, 23),
            "category": "Contract",
            'org': 'Freelance',
            'location': 'Astana (Kazakhstan)',
            'description': 'Built Python-based interactive data visualization dashboard for Risk Management department, which automated the reporting done previously by a manager in Excel every month (tech stack: Pandas, Flask, Dash)'
         },
        {
            "role": "Student - Master's degree in Business Analytics & Big Data",
            "start": date_axis(2019, 4, 23),
            "end": date_axis(2020, 3, 6),
            "category": 'Education',
            'org': 'IE University',
            'location': 'Madrid (Spain)',
            'description': """
                            • GPA: 3.91/4.0 (ranked 1st).
                            • IE Talent Scholarship.
                            • Delivered 2 Python workshops for non-technical students.
                            • Participated at IE Venture Lab, start-up accelerator for IE students and alumni. 
            """
         },
        {
            "role": "Global Graduate - Digital",
            "start": date_axis(2020, 8, 17),
            "end": date_axis(2022, 8, 17),
            "category": 'Full-time job',
            'org': 'Volvo Cars',
            'location': 'Gothenburg (Sweden)',
            'description': '• Global Graduate Program (2 years). • 1st rotation: Digital Strategy team.'
         },
        {
            'role': 'Traveler',
            'start': date_axis(2013, 7, 1),
            'end': date_axis(2013, 7, 8),
            'category': 'Tourism',
            'org': 'Travel',
            'location': 'Kemer (Turkey)',
            'description': 'Tourism with a friend',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2014, 6, 25),
            'end': date_axis(2014, 6, 26),
            'category': 'Tourism',
            'org': 'Travel',
            'location': 'Andorra',
            'description': 'Tourism with a host family',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2014, 7, 5),
            'end': date_axis(2014, 7, 13),
            'category': 'Tourism',
            'org': 'Travel',
            'location': 'Madrid-Pamplona-Bilbao (Spain)',
            'description': 'Visiting friends in Spain. San Fermin',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2015, 7, 16),
            'end': date_axis(2015, 7, 17),
            'category': 'Tourism',
            'org': 'Travel',
            'location': 'New York City (USA)',
            'description': 'Tourism with a friend',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2015, 7, 31),
            'end': date_axis(2015, 8, 2),
            'category': 'Tourism',
            'org': 'Travel',
            'location': 'San Francisco (USA)',
            'description': 'Tourism with a friend',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2015, 8, 12),
            'end': date_axis(2015, 8, 28),
            'category': 'Tourism',
            'org': 'Travel',
            'location': 'Mirabel-Paris-Viller Chatel (France), Milan-Venezia (Italy), Vienna (Austria)',
            'description': 'Visiting the host family from Toulouse, wedding of a friend in northern France, travel to Italy and Austria with my mom'
        },
        {
            'role': 'Traveler',
            'start': date_axis(2016, 5, 13),
            'end': date_axis(2016, 5, 20),
            'category': 'Tourism',
            'org': 'Travel',
            'location': 'Paris (France)',
            'description': 'Visiting friends',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2016, 6, 4),
            'end': date_axis(2016, 6, 8),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Munich (Germany)',
            'description': 'Meeting with Microsoft graduates from Central & Eastern Europe area',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2016, 7, 14),
            'end': date_axis(2016, 7, 23),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Orlando, FL (USA)',
            'description': 'First global training for Microsoft graduates, Microsoft Global Exchange event',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2016, 10, 9),
            'end': date_axis(2016, 10, 14),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Prague (Czech Republic)',
            'description': 'CEE Sales Academy training',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2017, 2, 26),
            'end': date_axis(2017, 3, 4),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Munich (Germany)',
            'description': 'Training for Microsoft security solutions',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2017, 2, 13),
            'end': date_axis(2017, 2, 16),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Baku (Azerbaijan)',
            'description': 'Regular customer meetings',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2017, 4, 17),
            'end': date_axis(2017, 4, 20),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Baku (Azerbaijan)',
            'description': 'Regular customer meetings',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2017, 5, 1),
            'end': date_axis(2017, 5, 4),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Baku (Azerbaijan)',
            'description': 'Regular customer meetings',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2017, 6, 20),
            'end': date_axis(2017, 6, 22),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Yerevan (Armenia)',
            'description': 'Regular customer meetings',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2017, 2, 13),
            'end': date_axis(2017, 2, 16),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Baku (Azerbaijan)',
            'description': 'Regular customer meetings',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2017, 7, 18),
            'end': date_axis(2017, 7, 22),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'London (UK)',
            'description': 'Customer reference visit',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2017, 8, 29),
            'end': date_axis(2017, 9, 8),
            'category': 'Tourism',
            'org': 'Travel',
            'location': 'Hong Kong',
            'description': 'Honeymoon',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2017, 10, 1),
            'end': date_axis(2017, 10, 6),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Budapest (Hungary)',
            'description': 'CEE Sales Academy training',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2017, 10, 9),
            'end': date_axis(2017, 10, 12),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Baku (Azerbaijan)',
            'description': 'Regular customer meetings',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2017, 10, 12),
            'end': date_axis(2017, 10, 13),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Minsk (Belarus)',
            'description': 'Regular customer meetings',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2017, 11, 30),
            'end': date_axis(2017, 12, 1),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Minsk (Belarus)',
            'description': 'Regular customer meetings',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2018, 1, 15),
            'end': date_axis(2018, 1, 17),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Baku (Azerbaijan)',
            'description': 'Regular customer meetings',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2018, 1, 19),
            'end': date_axis(2018, 2, 4),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Chicago-Seattle-New York City (USA)',
            'description': 'Microsoft Tech Ready training',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2018, 5, 7),
            'end': date_axis(2018, 5, 13),
            'category': 'Tourism',
            'org': 'Travel',
            'location': 'Tbilisi (Georgia)',
            'description': 'Travel with wife and Spanish friends',
        },
        {
            'role': 'Traveler',
            'start': date_axis(2020, 3, 8),
            'end': date_axis(2020, 3, 11),
            'category': 'Business trip',
            'org': 'Travel',
            'location': 'Gothenburg (Sweden)',
            'description': 'Volvo Cars Experience Days event',
        },
        {
            'role': 'Person',
            'start': date_axis(2016, 3, 15),
            'end': date_axis(2016, 3, 16),
            'category': 'Personal',
            'org': 'Key moments',
            'location': 'Kazakhstan',
            'description': 'Signed the contract with Microsoft'
        },
        {
            'role': 'Person',
            'start': date_axis(2013, 3, 13),
            'end': date_axis(2013, 3, 14),
            'category': 'Personal',
            'org': 'Key moments',
            'location': 'Kazakhstan',
            'description': 'Met my future wife'
        },
        {
            'role': 'Person',
            'start': date_axis(2017, 8, 18),
            'end': date_axis(2017, 8, 19),
            'category': 'Personal',
            'org': 'Key moments',
            'location': 'Kazakhstan',
            'description': 'Officially got married!'
        },
        {
            'role': 'Person',
            'start': date_axis(2017, 8, 25),
            'end': date_axis(2017, 8, 26),
            'category': 'Personal',
            'org': 'Key moments',
            'location': 'Kazakhstan',
            'description': '2-day wedding'
        },
        {
            'role': 'Person',
            'start': date_axis(2016, 6, 11),
            'end': date_axis(2016, 6, 12),
            'category': 'Personal',
            'org': 'Key moments',
            'location': 'Kazakhstan',
            'description': 'Graduation day at Nazarbayev University'
        },
        {
            'role': 'Person',
            'start': date_axis(2019, 4, 9),
            'end': date_axis(2019, 4, 10),
            'category': 'Personal',
            'org': 'Key moments',
            'location': 'Spain',
            'description': 'Moved to Madrid'
        },
        {
            'role': 'Person',
            'start': date_axis(2019, 9, 5),
            'end': date_axis(2019, 9, 6),
            'category': 'Personal',
            'org': 'Key moments',
            'location': 'Spain',
            'description': 'Became father for the first time!'
        },
        {
            'role': 'Person',
            'start': date_axis(2020, 3, 10),
            'end': date_axis(2020, 3, 11),
            'category': 'Personal',
            'org': 'Key moments',
            'location': 'Sweden',
            'description': 'Signed the contract with Volvo Cars'
        },
        {
            'role': 'Person',
            'start': date_axis(2020, 3, 6),
            'end': date_axis(2020, 3, 7),
            'category': 'Personal',
            'org': 'Key moments',
            'location': 'Spain',
            'description': 'Graduation day at IE University'
        },
        {
            'role': 'Person',
            'start': date_axis(2020, 3, 16),
            'end': date_axis(2020, 3, 17),
            'category': 'Personal',
            'org': 'Key moments',
            'location': 'Spain',
            'description': 'During heavy COVID-19 situation in Madrid, returned to Kazakhstan'
        },
    ])
    return pd.merge(data, colors, on='category')

@st.cache
def load_language():
    data = pd.DataFrame([
        {
            'language': 'English   ',
            'proficiency (LinkedIn)': 'Full professional proficiency', # LinkedIn convention
            'level': 84,
            'speaking proficiency': 'Fluent',
            'proficiency (CEFR)': 'C1',
            'comments': 'Undergraduate and graduate degrees completed in English.\nWork in international environments.\nConsume information mostly in English.'
        },
        {
            'language': 'Russian   ',
            'proficiency (LinkedIn)': 'Native or bilingual proficiency',
            'level': 100,
            'speaking proficiency': 'Native',
            'proficiency (CEFR)': 'C2',
            'comments': 'Mother tongue.'
        },
        {
            'language': 'French    ',
            'proficiency (LinkedIn)': 'Professional proficiency',
            'level': 67,
            'speaking proficiency': 'Fluent',
            'proficiency (CEFR)': 'B2',
            'comments': 'Lived 2 months in France.\nObtained DELF B2 certificate in 2015 with Speaking grade of 23/25.\nRoom for improvement: writing skills.'
        },
        {
            'language': 'Spanish   ',
            'proficiency (LinkedIn)': 'Professional proficiency',
            'level': 67,
            'speaking proficiency': 'Fluent',
            'proficiency (CEFR)': 'B2',
            'comments': 'Lived 1 year in Madrid, Spain.\nDid not get any certificates yet, but have experience passing interviews in Spanish.\nRoom for improvement: writing skills.'
        },
        {
            'language': 'Kazakh    ',
            'proficiency (LinkedIn)': 'Limited professional proficiency',
            'level': 50,
            'speaking proficiency': 'Proficient',
            'proficiency (CEFR)': 'B1',
            'comments': 'Conversational level of proficiency.'
        },
        {
            'language': 'Swedish   ',
            'proficiency (LinkedIn)': 'Elementary proficiency',
            'level': 33,
            'speaking proficiency': 'Beginner',
            'proficiency (CEFR)': 'A1',
            'comments': 'Started to learn in May 2020 (self-study).'
        },
    ])
    return data

@st.cache
def load_programming_lang():
    data = pd.DataFrame([
        {
            'programming language': 'Python',
            'level': 80,
            'definition': 'Can write the code',
            'comments': 'This website is written mostly in Python (streamlit). Used Flask, pandas, plotly in my freelance project. Used scikit-learn/PyTorch/Keras for Machine Learning projects.'
        },
        {
            'programming language': 'SQL',
            'level': 70,
            'definition': 'Can write the code',
            'comments': 'Can write sophisticated queries.'
        },
        {
            'programming language': 'R',
            'level': 60,
            'definition': 'Can write the code',
            'comments': 'Despite preferring pandas over data.table and scikit-learn over R packages for Machine Learning, I can use R if needed.'
        },
        {
            'programming language': 'HTML5/CSS',
            'level': 50,
            'definition': 'Can write some code',
            'comments': 'Used HTML and CSS in my freelance project and in this website.'
        },
        {
            'programming language': 'JavaScript',
            'level': 30,
            'definition': 'Can read the code',
            'comments': 'Had a course on JS, used it in a project.'
        }
    ])
    return data

@st.cache
def load_courses():
    data = pd.DataFrame([
        {
            'Course': 'Deep Learning Specialization',
            'Organization': 'deeplearning.ai',
            'Topic': 'Data Science / AI',
            'Platform': 'coursera.org',
            'Status': 'Completed',
            'Date': '2020-05-17',
            'Certificate': 'https://www.coursera.org/account/accomplishments/specialization/AVD5TJYKCR3L'
        },
        {
            'Course': 'Strategic Management of Innovation',
            'Organization': 'HEC Paris',
            'Topic': 'Business Strategy',
            'Platform': 'coursera.org',
            'Date': '2019-09-19',
            'Status': 'Completed',
            'Certificate': 'https://www.coursera.org/account/accomplishments/verify/H5E2CQW754W8',
        },
        {
            'Course': 'How to Build Digital Products',
            'Organization': 'Product School',
            'Topic': 'Other',
            'Platform': 'productschool.teachable.com',
            'Date': '2020-06-20',
            'Status': 'Completed',
            'Certificate': 'cert_kr5drxm0',
        },
        {
            'Course': 'How to Build and Grow Product Teams',
            'Organization': 'Product School',
            'Topic': 'Other',
            'Platform': 'productschool.teachable.com',
            'Date': '2020-09-01',
            'Status': 'In progress',
            'Certificate': '',
        },
        {
            'Course': 'Product Design',
            'Organization': 'Product School',
            'Topic': 'Design and UX/UI',
            'Platform': 'productschool.teachable.com',
            'Date': '2020-09-01',
            'Status': 'In progress',
            'Certificate': '',
        },
        {
            'Course': 'The Science of Everyday Thinking',
            'Organization': 'University of Queensland',
            'Topic': 'Other',
            'Platform': 'edx.com',
            'Date': '2014-07-02',
            'Status': 'Completed',
            'Certificate': 'https://verify.edx.org/cert/ca2ff3759ed84b4399ab34645e801ea0',
        },
        {
            'Course': 'Analyzing and Visualizing Data with Power BI',
            'Organization': 'Microsoft',
            'Topic': 'Analytics',
            'Platform': 'edx.com',
            'Date': '2016-12-28',
            'Status': 'Completed',
            'Certificate': 'https://courses.edx.org/certificates/8548fd38adfa4f68a940c54a45f89ada',
        },
        {
            'Course': 'Brand and Product Management',
            'Organization': 'IE Business School',
            'Topic': 'Marketing / Sales',
            'Platform': 'coursera.org',
            'Date': '2020-04-16',
            'Status': 'Completed',
            'Certificate': 'https://www.coursera.org/account/accomplishments/records/SSFASDY293QL',
        },
        {
            'Course': 'Data Scientist with Python track',
            'Organization': 'DataCamp',
            'Topic': 'Data Science / AI',
            'Platform': 'datacamp.com',
            'Date': '2019-06-10',
            'Status': 'Completed',
            'Certificate': 'https://www.datacamp.com/statement-of-accomplishment/track/65382807a81e490fa943aa8f06da188ca789e3eb'
        },
        {
            'Course': 'Learn Growth Hacking',
            'Organization': 'One Month',
            'Topic': "Marketing / Sales",
            'Platform': 'onemonth.com',
            'Date': '2019-10-15',
            'Status': 'Completed',
            'Certificate': ''
        },
        {
            'Course': 'Design Thinking',
            'Organization': 'IE Business School',
            'Topic': 'Design and UX/UI',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2019-11-01',
            'Certificate': ''
        },
        {
            'Course': 'Agile Project Management',
            'Organization': 'IE Business School',
            'Topic': 'Other',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2019-11-01',
            'Certificate': ''
        },
        {
            'Course': 'Analytics for Financial Services',
            'Organization': 'IE University',
            'Topic': 'Industry Knowledge',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2020-03-01',
            'Certificate': ''
        },
        {
            'Course': 'Analytics for Retail & Consumer',
            'Organization': 'IE University',
            'Topic': 'Industry Knowledge',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2020-03-01',
            'Certificate': ''
        },
        {
            'Course': 'Big Data & Health',
            'Organization': 'IE University',
            'Topic': 'Industry Knowledge',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2020-03-01',
            'Certificate': ''
        },
        {
            'Course': 'Marketing Intelligence',
            'Organization': 'IE University',
            'Topic': 'Marketing / Sales',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2020-03-01',
            'Certificate': ''
        },
        {
            'Course': 'Insight Selling',
            'Organization': 'Microsoft',
            'Topic': 'Marketing / Sales',
            'Platform': 'Microsoft (internal)',
            'Status': 'Completed',
            'Date': '2017-10-27',
            'Certificate': 'https://www.youracclaim.com/badges/1bcd0fd8-a58d-4527-875c-21af1d37002d/public_url'
        },
        {
            'Course': 'Entrepreneurial Management',
            'Organization': 'UW-Madison',
            'Topic': 'Other',
            'Platform': 'on-campus',
            'Status': 'Completed',
            'Date': '2015-08-09',
            'Certificate': ''
        },
        {
            'Course': 'Docker Fundamentals',
            'Organization': 'A Cloud Guru',
            'Topic': 'Other',
            'Platform': 'acloud.guru',
            'Status': 'Completed',
            'Date': '2020-07-30',
            'Certificate': ''
        }
    ])

    return data

@st.cache
def load_travel():
    data = pd.DataFrame([
        {
            'Year': '2005',
            "total": 3,
            "count": 2,
            "Countries I have been to (names)": 'Kazakhstan, Turkey',
            'New countries': 'Turkey'
        },
        {
            'Year': '2006',
            "total": 3,
            "count": 1,
            "Countries I have been to (names)": 'Kazakhstan',
            'New countries': ''
        },
        {
            'Year': '2007',
            "total": 4,
            "count": 2,
            "Countries I have been to (names)": 'Kazakhstan, Spain',
            'New countries': 'Spain'
        },
        {
            'Year': '2008',
            "total": 5,
            "count": 2,
            "Countries I have been to (names)": 'Kazakhstan, Bulgaria',
            "New countries": 'Bulgaria'
        },
        {
            'Year': '2009',
            "total": 6,
            "count": 2,
            "Countries I have been to (names)": 'Kazakhstan, United Arab Emirates',
            'New countries': 'United Arab Emirates'
        },
        {
            'Year': '2010',
            "total": 7,
            "count": 2,
            "Countries I have been to (names)": 'Kazakhstan, Thailand',
            'New countries': 'Thailand'
        },
        {
            'Year': '2011',
            "total": 11,
            "count": 5,
            "Countries I have been to (names)": 'Austria, France, Hungary, Kazakhstan, Switzerland',
            'New countries': 'Austria, France, Hungary, Switzerland'
        },
        {
            'Year': '2012',
            "total": 11,
            "count": 1,
            "Countries I have been to (names)": 'Kazakhstan',
            'New countries': ''
        },
        {
            'Year': '2013',
            "total": 12,
            "count": 3,
            "Countries I have been to (names)": 'Israel, Kazakhstan, Turkey',
            'New countries': 'Israel'
        },
        {
            'Year': '2014',
            "total": 13,
            "count": 4,
            "Countries I have been to (names)": 'Andorra, France, Kazakhstan, Spain',
            'New countries': 'Andorra'
        },
        {
            'Year': '2015',
            "total": 15,
            "count": 5,
            "Countries I have been to (names)": 'Austria, France, Italy, Kazakhstan, USA',
            'New countries': 'Italy, USA'
        },
        {
            'Year': '2016',
            "total": 17,
            "count": 5,
            "Countries I have been to (names)": 'Czech Republic, France, Germany, Kazakhstan, USA',
            'New countries': 'Czech Republic, Germany'
        },
        {
            'Year': '2017',
            "total": 22,
            "count": 8,
            "Countries I have been to (names)": 'Armenia, Azerbaijan, Belarus, Germany, Hong Kong, Hungary, Kazakhstan, UK',
            'New countries': 'Armenia, Azerbaijan, Belarus, Hong Kong, UK'
        },
        {
            'Year': '2018',
            "total": 23,
            "count": 4,
            "Countries I have been to (names)": 'Azerbaijan, Georgia, Kazakhstan, USA',
            'New countries': 'Georgia'
        },
        {
            'Year': '2019',
            "total": 23,
            "count": 2,
            "Countries I have been to (names)": 'Kazakhstan, Spain',
            'New countries': ''
        },
        {
            'Year': '2020',
            "total": 24,
            "count": 4,
            "Countries I have been to (names)": 'Kazakhstan, Spain, Sweden, Russia',
            'New countries': 'Sweden'
        },
    ])

    return data