import os
import sys


from src.entity.artifact_entity import ClassificationMetricArtifact
from src.exception.exception import CustomException
from sklearn.metrics import recall_score,precision_score,f1_score


def get_classification_score(y_true,y_pred)->ClassificationMetricArtifact:
    try:
        
        model_f1_score = f1_score(y_true,y_pred)
        model_presicion_score = precision_score(y_true,y_pred)
        model_recall_score = recall_score(y_true,y_pred)

        classifiaction_metric_artifact = ClassificationMetricArtifact(
            f1_score=model_f1_score,
            precision_score=model_presicion_score,
            recall_score=model_recall_score
        )

        return classifiaction_metric_artifact

    except Exception as e:
        raise CustomException(e,sys)