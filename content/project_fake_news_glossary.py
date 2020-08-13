from utils import img_html

nlp_glossary = f"""
        <details class="">
        <summary><i>Glossary of NLP concepts</i></summary>
        <br/>
        <div>
            <strong>Corpus</strong>: set of <i>documents</i> (our dataset of news with <i>fake</i> and <i>real</i> labels).
        </div>
        <div>
            <strong>Documents</strong>: basic unit or object (a particular news or tweet).
        </div>
        <div>
            <strong>Part-of-speech (POS) tagging</strong>: an identification of words as nouns, verbs, adjectives, adverbs, etc. 
            Full list of Universal POS tags used by spaCy can be found <a href='https://spacy.io/api/annotation' target='_blank'>here</a>.
        </div>
        <div>
            <strong>Bag-of-Words (BoW) representation</strong>: representation of documents as a collection words with count value for each word.
            In this representation, what is important is how many times a particular word appears in the corpus and in each document, but not the order of words. 
            There are 3 main ways to calculate <i>count value</i> for each word: <i>binary weighting</i>, <i>TF weighting</i>, and <i>TF-IDF weighting</i>
        </div>
        <div class='text-center'>
            {img_html('media/project-fake-news-bow-repr.png', 'max-width:50%', 'img-fluid')}
        </div>
        <div>
            <strong>Binary weighting</strong>: the count value is binary indicator (does this word exist in this document?)
        </div>
        <div class='text-center'>
            {img_html('media/project-fake-news-binary-w.png', 'max-width:50%', 'img-fluid')}
        </div>
        <div>
            <strong>Term Frequency (TF) weighting</strong>: the count value is just frequency of a word (how many times does this word appear in this document?).
        </div>
        <div class='text-center'>
            {img_html('media/project-fake-news-tf-w.png', 'max-width:50%', 'img-fluid')}
        </div>
        <div>
            <strong>Term Frequency-Inverse Document Frequency (TF-IDF) weighting</strong>: in TF weighting the words like articles (the, a) appear a lot in each document, which bring little information to distinguish documents. 
            We want rare words, because they are more informative that frequent ones (articles, pronouns, etc). 
            We can solve this problem by taking into account the number of documents in which they appear. 
            Therefore, the count value is real-valued number that is proportional to frequency of a word in this document and inversely proportionally to frequency of documents in which this word appears.
        </div>
        <div class='text-center'>
            {img_html('media/project-fake-news-tf-idf-w.png', 'max-width:50%', 'img-fluid')}
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