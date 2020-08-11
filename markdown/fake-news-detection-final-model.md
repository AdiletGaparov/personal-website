```python
class FakeNewsDetection():
    
    def __init__(self, max_features_lemma=80000, max_features_pos=20000):
        self.tfidf_lemma = TfidfVectorizer(ngram_range=(1,2), 
                              tokenizer=lambda doc: doc, 
                              preprocessor=lambda doc:doc, 
                              max_features=max_features_lemma)
        
        self.tfidf_pos = TfidfVectorizer(ngram_range=(4,4), 
                              tokenizer=lambda doc: doc, 
                              preprocessor=lambda doc:doc, 
                              max_features=max_features_pos)
        
    def fit(self, X_lemma, X_pos, labels=None):
        
        X_lemma = self.tfidf_lemma.fit_transform(X_lemma)
        X_lemma = pd.DataFrame(X_lemma.A, columns=self.tfidf_lemma.get_feature_names())
        
        X_pos = self.tfidf_pos.fit_transform(X_pos)
        X_pos = pd.DataFrame(X_pos.A, columns=self.tfidf_pos.get_feature_names())
        
        X_prep = pd.concat([X_lemma, X_pos], axis=1)
        
        self.model = VotingClassifier(estimators=[('NB', MultinomialNB(alpha=0.1)), 
                                     ('SVM', LinearSVC(C=1, random_state=289, loss='hinge')), 
                                     ('SGD', SGDClassifier(random_state=289, loss='hinge'))], 
                                      voting='hard', 
                                      n_jobs=-1)
        
        self.model.fit(X_prep, labels)
        

    def predict(self, X_lemma, X_pos):
        
        X_lemma = self.tfidf_lemma.transform(X_lemma)
        X_lemma = pd.DataFrame(X_lemma.A, columns=self.tfidf_lemma.get_feature_names())
        
        X_pos = self.tfidf_pos.transform(X_pos)
        X_pos = pd.DataFrame(X_pos.A, columns=self.tfidf_pos.get_feature_names())
        
        X_prep = pd.concat([X_lemma, X_pos], axis=1)
        
        predictions = self.model.predict(X_prep)
        predictions = pd.Series(predictions)
        predictions = predictions.replace([0,1], ['FAKE', 'REAL']).to_list()
        
        return predictions
        
    def predict_from_raw(self, news):
        
        news_lemma, news_pos = spacy_tokenizer(news)
        
        news_lemma = self.tfidf_lemma.transform(news_lemma)
        news_lemma = pd.DataFrame(news_lemma.A, columns=self.tfidf_lemma.get_feature_names())
        
        news_pos = self.tfidf_pos.transform(news_pos)
        news_pos = pd.DataFrame(news_pos.A, columns=self.tfidf_pos.get_feature_names())
        
        news_prep = pd.concat([news_lemma, news_pos], axis=1)
        
        predictions = self.model.predict(news_prep)
        predictions = pd.Series(predictions)
        predictions = predictions.replace([0,1], ['FAKE', 'REAL']).to_list()
        
        return predictions
```