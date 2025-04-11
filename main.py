import numpy as np

from utils import (
    compute_confusion_matrix,
    compute_counts,
    compute_metrics,
    f1_score,
    precision,
    recall,
    specificity
)

cls_index = 1
preds = np.array([1, 2, 1, 3, 3, 0, 0, 1, 2])
labels = np.array([1, 2, 2, 3, 2, 0, 1, 1, 3])

matrix = compute_confusion_matrix(preds, labels)
count_dict = compute_counts(matrix, cls_index)

print("\nPrecision 1: ", compute_metrics(count_dict, "precision"))
print("Precision 2: ", precision(preds, labels, True, cls_index))

print("\nRecall 1: ", compute_metrics(count_dict, "recall"))
print("Recall 2: ", recall(preds, labels, True, cls_index))

print("\nSpecificity 1: ", compute_metrics(count_dict, "specificity"))
print("Specificity 2: ", specificity(preds, labels, True, cls_index))

print("\nF1 Score 1: ", compute_metrics(count_dict, "f1"))
print("F1 Score 2: ", f1_score(preds, labels, True, cls_index))
