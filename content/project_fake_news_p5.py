from utils import img_html

project_fake_news_p5 = f"""
<details>
<summary><strong>5. Evaluation</strong></summary><br/>
<div>For every model:
<ul>
    <li><i>Unigrams + Bigrams</i> are better than just <i>Unigrams</i>.</li>
    <li><i>Unigrams + Bigrams + POS-tags</i> are better than <i>Unigrams + Bigrams</i>.</li>
</ul>
After optimizing all models, I combined all 3 of them using <a href='https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html'>Voting Classifier</a>. Voting Classifier gave slightly better results than others.  
</div>
<div>{img_html('media/project-fake-news-evaluation.png', 'max-width:100%', 'img-fluid')}</div>
<br/>
</details>    
"""