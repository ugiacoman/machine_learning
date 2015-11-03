#Spam filtering/text classification


##Classifier Summaries

###c50:

For c50, we increased the boosting. Boosting is the process of adding weak learners in such a way that newer learners pick up the slack of older learners. In this way we can increase the accuracy of the model. So, we increased the number of boosting iterations by increasing the trials parameter from 10 to 100.

True positive rate:   0.9778085992 <br>
False positive rate:  0.06471816284 <br>
True negative rate:   0.9352818372 <br>
False negative rate:  0.02219140083 <br>
Misclassification rate:  0.03916666667 <br>

###kNN:

For kNN, the choice of k depends upon the data. Generally, the larger values of k reduce the effect of noise on the classification. However, during our experiments, we were able to find less noise with a lower k. We decreased k from 5 to 1.

True positive rate:   0.8377253814 <br>
False positive rate:  0.2338204593 <br>
True negative rate:   0.7661795407 <br>
False negative rate:  0.1622746186 <br>
Misclassification rate:  0.1908333333 <br>

###svm:

For svm, we improved the tuning on the model by increasing the list of parameter vectors spanning the sampling space.

True positive rate:   0.9625520111 <br>
False positive rate:  0.1002087683 <br>
True negative rate:   0.8997912317 <br>
False negative rate:  0.0374479889 <br>
Misclassification rate:  0.0625 <br>

###nn:

We were not able to improve the misclassification rate for the neural network. 

True positive rate:   0.9611650485 <br>
False positive rate:  0.108559499 <br>
True negative rate:   0.891440501 <br>
False negative rate:  0.03883495146 <br>
Misclassification rate:  0.06666666667 <br>

##Performance

Performance was by far the greatest in our c50 classifier.

Classifier  | Misclassification rate
------------- | -------------
c50  | 0.03916666667
svm  | 0.0625 
nn   | 0.06666666667
kNN  | 0.1908333333


4) On the basis of your results, recommend one or more classifier, and explain your rationale.


TODO: 
	1) Create a random training set and test set
		2) Think about false positives
	2)