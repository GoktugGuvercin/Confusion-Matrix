
# Confusion Matrix

In classification problems, the models classify the samples into predefined categories. To evaluate how well these models perform, we use confusion matrix. While the rows represent the predictions, columns refer to the ground-truth labels. Initially, all entries of this matrix are set to zero. Then, each prediction is compared with its true label, and the corresponding cell in the matrix is incremented by one. 

In binary classification problems, there are only two categories, usually labeled as positive ($1$) and negative ($0$). Multi-class classification problems do not inherently involve positive and negative terminology; nevertheless, to be able to compute performance metrics *TP*, *FP*, *FN*, and *TN* one class is selected as the positive class while the others are collectively considered negative. This approach, known as one-versus-all strategy,requires computing these metrics separately for each class.

- *TP:* Hits
- *FP:* False Alarm (Type 1 Error)
- *FN:* Miss (Type 2 Error)
- *TN:* Correct Rejections

## Classification Metrics

- Accuracy: It measures the proportion of correct predictions.

$$\frac{TP + TN}{TP + TN + FP + FN}$$

- Precision: It reflects the ability of predicting positiveness. It calculates how many of positive predictions are correct. So, it quantifies how reliable positive predictions are.

$$\frac{TP}{TP + FP}$$

- Recall: It is generally known as hit rate or true positive rate. It calculates how many positive labels are correctly predicted. 

$$\frac{TP}{TP + FN}$$

- Specificity: It is called as true negative rate. It calculates how many negative labels are correctly predicted.

$$\frac{TN}{TN + FP}$$

- F1 Score: It is harmoic mean of precision and recall, where relative contribution of both measurements are equal. The models are expected to achieve good scores in both precision and recall. F1 score contracts 2 metrics into one. In that way, you would become capable of making comparison between the models in terms of both metrics at the same time.

$$ \frac{2}{\frac{1}{Pre} + \frac{1}{Rec}} = \frac{2 \cdot Pre \cdot Rec}{Pre + Rec} = \frac{2 \cdot TP}{2 \cdot TP + FP + FN}$$

We can use the following interpretations to understand the computations of these metrics:

- *TP + FP*: Number of positive predictions
- *TP + FN*: Number of positive labels
- *TN + FP*: Number of negative labels


## Segmentation Metrics

Image segmentation aims to parition the image into meaningful regions. At this point, each pixel is classified into a particular category, either in binary or multi-class manner. In **semantic segmentation**, all objects of same class are treated identically. On the other hand, **instance segmentation** pays high attention to the separation of different instances of same object. 

Ultimately, segmentation is classification problem at the pixel level; that is why, all classification metrics are applicable. Predicted and ground-truth masks are compared to each other in calculation of these metrics. Overlapping regions refer to *true positive* and *true negative* regions, while non-overlapping spots indicate *false positive* or *false negative*. The number of pixels in these regions help to calculate total counting scores for TP, FP, FN, and TN. In that way, all classification metrics can be easily computed. Aside from classification, we also have 2 segmentation metrics, which are dice score and jaccard index:

$$DSC = \frac{2 |A \cap B|}{|A| + |B|} = \frac{2 \cdot TP}{2 \cdot TP + FP + FN}$$ 
$$JI = \frac{2 |A \cap B|}{|A \cup B|} = \frac{TP}{TP + FP + FN}$$

<p align="center">
  <img src="https://github.com/GoktugGuvercin/Confusion-Matrix/blob/main/images/Segmentation.png" width="700" title="Segmentation">
</p>
