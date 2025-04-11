import numpy as np

Array = np.ndarray


def compute_confusion_matrix(preds: Array, labels: Array) -> Array:

    num_classes = labels.max() + 1
    matrix = np.zeros((num_classes, num_classes))

    # preds: rows, labels: columns
    for pred, label in zip(preds, labels):
        matrix[pred, label] += 1
    return matrix


def compute_counts(matrix: Array, cls_index: int) -> dict:

    class_indices = [i for i in range(matrix.shape[0])]
    class_indices.remove(cls_index)

    tp = int(matrix[cls_index, cls_index])
    fp = int(matrix[cls_index, class_indices].sum())
    fn = int(matrix[class_indices, cls_index].sum())
    tn = int(matrix.sum() - (tp + fp + fn))

    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn}


def compute_metrics(count_dict: dict, metric: str) -> float:

    tp, fp = count_dict["tp"], count_dict["fp"]
    fn, tn = count_dict["fn"], count_dict["tn"]

    if metric == "precision":
        return tp / (tp + fp)
    elif metric == "recall":
        return tp / (tp + fn)
    elif metric == "specificity":
        return tn / (tn + fp)
    elif metric == "f1":
        return 2 * tp / (2 * tp + fp + fn)
    else:
        return -1.0


def accuracy(preds: Array, labels: Array) -> float:
    compare = (preds == labels).astype(int)
    return compare.sum() / len(compare)


def precision(
        preds: Array,
        labels: Array,
        to_binary: bool,
        cls_index: int) -> float:

    if to_binary:
        preds = (preds == cls_index).astype(int)
        labels = (labels == cls_index).astype(int)
    return (preds * labels).sum() / preds.sum()


def recall(preds: Array,
           labels: Array,
           to_binary: bool,
           cls_index: int) -> float:

    if to_binary:
        preds = (preds == cls_index).astype(int)
        labels = (labels == cls_index).astype(int)
    return (preds * labels).sum() / labels.sum()


def specificity(preds: Array,
                labels: Array,
                to_binary: bool,
                cls_index: int) -> float:

    if to_binary:
        preds = (preds != cls_index).astype(int)
        labels = (labels != cls_index).astype(int)
    return (preds * labels).sum() / labels.sum()


def f1_score(preds: Array,
             labels: Array,
             to_binary: bool,
             cls_index: int) -> float:

    prec = precision(preds, labels, to_binary, cls_index)
    rec = recall(preds, labels, to_binary, cls_index)
    return (2 * prec * rec) / (prec + rec)
