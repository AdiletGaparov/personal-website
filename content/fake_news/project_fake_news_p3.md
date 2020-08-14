<details>
<summary><strong>3. Data Preparation</strong></summary><br/> 

I built two custom _tokenizers_ using [spaCy](https://spacy.io/) library and their medium-size pre-trained statistical model for English, because it was trained on web-content (blogs, news, comments):    
* To get _lemmas_ of _tokens_, which are not corresponding to _POS tags_ `SPACE`, `PUNCT` (punctuation: .,:?), `X` (other: xasdasdg), `NUM` (numeral: 1, 2017, one, IV), `SYM` (symbol: $,§,©,,−,÷,=,😝), `DET` (determiner: a,an,the), `PART` (particle: 's,not).
* To get only _POS tags_

Since one of the hypotheses is that `fake` and `real` news use different words, it is important to remove _stopwords_ to better see the difference.

```python
import spacy
from nltk.corpus import stopwords

def spacy_tokenizer(data, n_process=4, pos=True, stop_words=True):
    """Tokenizes the data using spaCy. If pos=True, returns POS-tags too.

    Args:
        data (List): List of documents
        n_process (int): number of processes to run .pipe method of spaCy object
        pos (bool): if True, returns POS-tags too
        stop_words (bool): if True, remove stop words using NLTK Stopwords list

    Returns:
        List: List of lemmatized tokens
        List: List of POS-tags if pos=True
    """
    
    if stop_words == True:
        nltk_stopwords = stopwords.words("English")

    if spacy.__version__ < "2.2.2":
        data_gen = nlp.pipe(data, n_threads=n_process)
    else:
        data_gen = nlp.pipe(data, n_process=n_process)

    data_lemma = []

    if pos == True:
        data_pos = []

    for token_objects in data_gen:

        lemma_tokens = [
            token.lemma_.lower().strip()
            for token in token_objects
            if not wrong_token(token)
        ]

        if stop_words == True:
            lemma_tokens = [
                token for token in lemma_tokens if token not in nltk_stopwords
            ]

        data_lemma.append(lemma_tokens)

        if pos == True:
            pos_tokens = [token.pos_ for token in token_objects]
            data_pos.append(pos_tokens)
    
    if pos:
        return data_lemma, data_pos
    else:
        return data_lemma

def wrong_token(token):
    """Filters token based on POS-tag"""

    wrong_pos = token.pos_ in [
        "SPACE",
        "PUNCT",
        "X",
        "NUM",
        "SYM",
        "DET",
        "PART",
        "INTJ",
    ]
    personal_pronoun = token.lemma_ == "-PRON-"

    return personal_pronoun or wrong_pos
```

</details>
