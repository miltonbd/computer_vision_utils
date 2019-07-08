import numpy as np
from sklearn import metrics

def f1_score(y_label, y_pred):
    f1_score = metrics.f1_score(y_true=y_label, y_pred=y_pred)
    return f1_score

if __name__ == "__main__":
    y_label  = np.random.randint(0,2,(100,))
    y_pred = np.random.randint(0,2,(100,))
    f1_score = f1_score(y_label, y_pred)
    print(f1_score)