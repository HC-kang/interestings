import numpy as np
import matplotlib.pyplot as plt


s = np.random.poisson(5, 10000)

count, bins, ignored = plt.hist(s, 14, color='y')
plt.show()


#################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score


# ROC curve function
def roc_curve_plot(fpr, tpr): # false positive rate, true positive rate
    plt.plot(fpr, tpr, color = 'yellow', label = 'ROC')
    plt.plot([0,1], [0,1], color = 'darkblue', linestyle = '--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc = 'best')
    plt.show()


# number of sample : 1000
data_X, class_label = make_classification(n_samples = 1000, n_classes = 2, weights = [1,1], random_state = 1)

train_X, test_X, train_y, test_y = train_test_split(data_X, class_label, train_size = 0.2, random_state=1)


# 모델 만들기
model = RandomForestClassifier()
model.fit(train_X, train_y)


# 모델 성능평가
prob = model.predict_proba(test_X)

probs = prob[:,1]
probs


# AUC
auc = roc_auc_score(test_y, probs)

fpr, tpr, threshold = roc_curve(test_y, probs)

roc_curve_plot(fpr, tpr)

auc