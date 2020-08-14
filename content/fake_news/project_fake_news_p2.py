from utils import img_html

project_fake_news_p2 = f"""
<details>
<summary><strong>2. Data Understanding</strong></summary><br/>
<div>The dataset contains <span class='text-success bg-light'>3999</span> news articles (title + text) collected from the web with labels either <span class='text-success bg-light'>fake</span> or <span class='text-success bg-light'>real</span> (around 50-50 split).
<br/><br/>
I had several hypotheses on how <span class='text-success bg-light'>fake</span> news might be different from <span class='text-success bg-light'>real</span> news:   
<ol>
    <li>Talking about the same topic (i.e. politics), in <span class='text-success bg-light'>fake</span> news an author might use different words and <i>n-grams</i> (less formal).</li>
    <li><span class='text-success bg-light'>Fake</span> news might be mostly about politics and crime, hence completely different words and <i>n-grams</i> are used.</li>
    <li>In <span class='text-success bg-light'>fake</span> news an author might use different <i>POS tags</i>, i.e. more adjectives and adverbs, like incredibly or breaking.</li>
    <li><span class='text-success bg-light'>Real</span> news might be longer, because they tend to include supporting facts and references.</li>
</ol>
</div>
<div>
Summary of exploratory data analysis (EDA) on the dataset: 
<ul>
<li>
By plotting average <i>TF-IDF</i> values for the top 50 words by each class (<span class='text-success bg-light'>fake/real</span>), in the dataset there is slight difference between the words used, although the difference is not that clear for <i>unigrams</i>.</li>  
<div class='text-center'>{img_html('media/project-fake-news-unigrams.png','max-width:100%','img-fluid')}</div>
<li>This difference becomes clearer for <i>bigrams</i>.</li>
<div class='text-center'>{img_html('media/project-fake-news-bigrams.png','max-width:100%','img-fluid')}</div>
<li>There is also difference between <span class='text-success bg-light'>fake</span> and <span class='text-success bg-light'>real</span> news in terms of what <i>POS-tags</i> are used. Moreover, <span class='text-success bg-light'>fake</span> news seem to contain more <span class='text-success bg-light'>SYM</span> (symbols like $, %, §, ©, 😝), <span class='text-success bg-light'>X</span> (other like sfpksdpsxmsa), <span class='text-success bg-light'>INTJ</span> (interjection like psst, ouch, bravo, hello).</li>
<div class='text-center'>{img_html('media/project-fake-news-pos-tags.png', 'max-width:100%', 'img-fluid')}</div>
<li><span class='text-success bg-light'>Real</span> news tend to have more <i>tokens</i> and characters.</li>
<div class='text-center'>{img_html('media/project-fake-news-table.png', 'max-width:70%', 'img-fluid')}</div>
</ul>
<br/>
</details>
"""