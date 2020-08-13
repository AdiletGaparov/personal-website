<details>
<summary><strong>4. Modelling</strong></summary><br/>

The approach for the modeling was the following:        
1. Start with creating a classification model using only _TF-IDF_ values of _unigrams_.    
2. Create a model using _bigrams_.    
3. Combine _unigrams_ and _bigrams_ to see if the model improves.    
4. Build a model using only _POS-tags_.    
5. Combine _POS-tags_ and the _unigrams_/_bigrams_ to see if the model improves.    

The above procedure was repeated for each of the following Machine Learning algorithms from [scikit-learn](https://scikit-learn.org/stable/) library:   
* [Linear classifiers with SGD training.](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html)   
* [Naive Bayes classifier for multinomial models](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB)
* [Linear Support Vector Classification.](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html)

Grid Search was used to find the optimal hyperparameters for each model. 

</details>