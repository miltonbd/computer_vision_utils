import numpy as np
import matplotlib.pyplot as plt
from sklearn import  metrics

y_label = np.random.randint(0, 2, (100,))
y_pred = np.random.randint(0, 2, (100,))
precision_vs_recall  = metrics.precision_recall_curve(y_label, y_pred)
metrics.accuracy_score()
print(precision_vs_recall)