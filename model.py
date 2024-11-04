from sklearn.ensemble import BaggingClassifier # https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier
from sklearn.ensemble import RandomForestClassifier #https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier #https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier
from sklearn.ensemble import VotingClassifier #https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier
from sklearn.naive_bayes import GaussianNB #https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB
from sklearn.neighbors import KNeighborsClassifier #https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier
from sklearn.neural_network import MLPClassifier #https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
from lineartree import LinearTreeClassifier, LinearForestClassifier, LinearBoostClassifier #https://github.com/cerlymarco/linear-tree
from sklearn.svm import SVC #https://scikit-learn.org/1.5/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC
from sklearn.tree import DecisionTreeClassifier #https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
from sklearn.linear_model import RidgeClassifier, Ridge
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import log_loss
import numpy as np
import warnings
warnings.simplefilter('ignore')

models = {
    "BaggingClassifier": BaggingClassifier(),
    "RandomForestClassifier": RandomForestClassifier(),
    "ExtraTreesClassifier": ExtraTreesClassifier(),
    "GaussianNB": GaussianNB(),
    "NearestNeighborsClassifier": KNeighborsClassifier(),
    "MLPClassifier": MLPClassifier(),
    "LinearTreeClassifier": LinearTreeClassifier(base_estimator=RidgeClassifier()),
    "LinearForestClassifier": OneVsRestClassifier(LinearForestClassifier(Ridge(), max_features="sqrt")),
    "LinearBoostClassifier": LinearBoostClassifier(base_estimator=RidgeClassifier()),
    "VotingClassifier": VotingClassifier(estimators=[("BC", BaggingClassifier()), ("RFC", RandomForestClassifier()),("LFC", OneVsRestClassifier(LinearForestClassifier(Ridge(), max_features="sqrt")))], voting="soft"),
    "DecisionTreeClassifier": DecisionTreeClassifier()
}

def train_models(models, X_train, X_test, y_train, y_test):
    print("Training models...")
    for name, model in models.items():
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(X_test)
            log_loss_proba = log_loss(y_test, proba)
            print(f"{name} - {score} - {log_loss_proba}")
        else:
            print(f"{name} - {score}")