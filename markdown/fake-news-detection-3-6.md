<div class="shadow p-3 mb-5 bg-white rounded">

3. **Data Preparation**

For data preprocessing I am going to use [spaCy](https://spacy.io/) library and their medium-size pre-trained statistical model for English, because it was trained on web-content (blogs, news, comments).

I had several hypotheses on how *FAKE* news might be different from *REAL* news:   
1. Talking about the same topic (i.e. politics), in *FAKE* news an author might use different words and n-grams (less formal).   
2. *FAKE* news might be mostly about politics and crime, hence completely different words and n-grams are used.   
3. In FAKE news an author might use different POS tags, i.e. more adjectives and adverbs, like incredibly, breaking
To test those hypotheses, we will build two custom tokenizers:

To get Lemmas of tokens, which are not corresponding to POS tags SPACE, PUNCT, X, NUM, SYM, DET, PART
To get only POS tags
Since one of our hypotheses is that FAKE and REAL news use different words, it is important to remove stop-words to better see the difference.

</div>