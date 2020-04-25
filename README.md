# Reddit Flair Detector

Data Collection was done using PRAW ( Python Reddit API Wrapper)  which provied data for all the different flairs used in the project, Additionally this data was stored in an Instance of MongoDB, beause of the benfits MongoDB provides like faster access and queries.

Data was then cleaned and formatted and stored in data.csv for Exploratory Data Analysis then after EDA different types of classification algorithms were tested on the dataset to find the one with highest accuracy, the classification algorithms used were:

### 1.Logistic Regression
### 2.Naive Bayes Classifier
### 3.Linear SVM
### 4.Random Forest
### 5.Multi-Layer Perceptron Classifier

#These were tested on the dataset by the following methods:
### 1.Using 'title' as a feature
### 2.Using 'comment' as a feature
### 3.Using 'URL' as a feature
### 4.Using 'body' as a feature
### 5.combining all of the above  as a feature

Models/Features	           title	comment	 URL 	  body	 combined
Linear SVM	               0.802	0.561	   0.634	0.387  0.805
Naive Bayes Classifier	   0.713	0.506	   0.585	0.54	 0.61
Logistic Regression	       0.823	0.579	   0.649	0.521	 0.82
Random Forest	             0.811	0.567	   0.619	0.555	 0.835
MLP Classifier	           0.762	0.512	   0.591	0.521	 0.735


It was found that by combining all the features, the models performed significantly better, so all features were combined out of the five classification models that we had built earlier it was observed that ### Random Forest gave the best accuracy but the problem was the size of the model's file (RF.pkl) which as too big to be uploaded on github therefore, we used the second best model ### Logistics Regression

Then the web Application was built using Flask 
the application has an endpoint(/autmated_testing ) for testing the classifier autmatically 
the application has been deployed on Heroku 
link:- https://flair-classifier.herokuapp.com/
