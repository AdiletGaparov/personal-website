---
<div class="shadow p-3 mb-5 bg-white rounded">

**Individual project for Natural Language Processing (NLP) class at IE**

In this project, I am going to use CRoss-Industry Standard Process for Data Mining [(CRISP-DM methodology)](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining).   

1. **Business/Problem Understanding**

Fake News Detection is quite popular problem nowadays. There is no doubt that it is very complex problem, because we see that even major platforms can't efficiently stop the spread of fake news, hiring many people, deploying sophisticated policies and models.
For example, few years ago Twitter acquired startup Fabula AI, that has developed a technology to detect the fake information using graph-based approach, analyzing the differences in the way fake and real information spread across the network. 
Another (simpler) approach would be to analyze the difference in the choice of words used in both fake and real news. And this is what I did. 

2. **Data Understanding**   

The dataset contains `3999` news articles (title + text) collected from the web with labels either `fake` or `real` (around 50-50 split). 

I had several hypotheses on how `fake` news might be different from `real` news:   
1. Talking about the same topic (i.e. politics), in `fake` news an author might use different words and _n-grams_ (less formal).   
2. `Fake` news might be mostly about politics and crime, hence completely different words and _n-grams_ are used.   
3. In `fake` news an author might use different _POS tags_, i.e. more adjectives and adverbs, like incredibly or breaking.

To test these hypotheses, I built two custom _tokenizers_ using [spaCy](https://spacy.io/) library and their medium-size pre-trained statistical model for English, because it was trained on web-content (blogs, news, comments):    
* To get _lemmas_ of _tokens_, which are not corresponding to _POS tags_ `SPACE`, `PUNCT` (punctuation: .,:?), `X` (other: xasdasdg), `NUM` (numeral: 1, 2017, one, IV), `SYM` (symbol: $,§,©,,−,÷,=,😝), `DET` (determiner: a,an,the), `PART` (particle: 's,not).
* To get only _POS tags_

Since one of our hypotheses is that `fake` and `real` news use different words, it is important to remove _stopwords_ to better see the difference.

</div>