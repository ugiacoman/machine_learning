#Spam filtering/text classification


##Classifier Summaries

###c50

For c50, we increased the boosting. Boosting is the process of adding weak learners in such a way that newer learners pick up the slack of older learners. In this way we can increase the accuracy of the model. So, we increased the number of boosting iterations by increasing the trials parameter from 10 to 100.

True positive rate:   0.9778085992 <br>
False positive rate:  0.06471816284 <br>
True negative rate:   0.9352818372 <br>
False negative rate:  0.02219140083 <br>
Misclassification rate:  0.03916666667 <br>

###kNN

For kNN, the choice of k depends upon the data. Generally, the larger values of k reduce the effect of noise on the classification. However, during our experiments, we were able to find less noise with a lower k. We decreased k from 5 to 1.

True positive rate:   0.839112344 <br>
False positive rate:  0.2338204593 <br>
True negative rate:   0.7661795407 <br>
False negative rate:  0.160887656 <br>
Misclassification rate:  0.19 <br>

###svm

True positive rate:   0.9611650485 <br>
False positive rate:  0.1022964509 <br>
True negative rate:   0.8977035491 <br>
False negative rate:  0.03883495146 <br>
Misclassification rate:  0.06416666667 <br>

###nn

True positive rate:   0.9611650485 <br>
False positive rate:  0.108559499 <br>
True negative rate:   0.891440501 <br>
False negative rate:  0.03883495146 <br>
Misclassification rate:  0.06666666667 <br>

##Performance

2) knobs you played with in training each classifier
3) summaries of performance for each classifier, 
	- including total misclassification rate
	- the false positive and false negative rates
	- a confusion table. 
4) On the basis of your results, recommend one or more classifier, and explain your rationale.


TODO: 
	1) Create a random training set and test set
		2) Think about false positives
	2)