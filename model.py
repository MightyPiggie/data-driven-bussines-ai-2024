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
from sklearn.model_selection import ParameterGrid
import numpy as np
import warnings
warnings.simplefilter('ignore')

models = {
    "BaggingClassifier": BaggingClassifier(n_jobs=4),
    "RandomForestClassifier": RandomForestClassifier(n_jobs=4),
    "ExtraTreesClassifier": ExtraTreesClassifier(n_jobs=4),
    "GaussianNB": GaussianNB(),
    "NearestNeighborsClassifier": KNeighborsClassifier(n_jobs=4),
    "MLPClassifier": MLPClassifier(),
    "LinearTreeClassifier": LinearTreeClassifier(base_estimator=RidgeClassifier(), n_jobs=4),
    "LinearForestClassifier": OneVsRestClassifier(LinearForestClassifier(Ridge(), max_features="sqrt"), n_jobs=4),
    "LinearBoostClassifier": LinearBoostClassifier(base_estimator=RidgeClassifier()),
    "VotingClassifier": VotingClassifier(estimators=[("BC", BaggingClassifier()), ("RFC", RandomForestClassifier()),("LFC", OneVsRestClassifier(LinearForestClassifier(Ridge(), max_features="sqrt")))], voting="soft", n_jobs=4),
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

# BC_Parameters = {'estimator': [LinearTreeClassifier(base_estimator=RidgeClassifier()), OneVsRestClassifier(LinearForestClassifier(Ridge(), max_features="sqrt")), RandomForestClassifier(), ExtraTreesClassifier(), MLPClassifier(), KNeighborsClassifier(), GaussianNB()], 'n_estimators': [10, 50, 100], 'max_samples': [0.5, 1.0], 'max_features': [0.5, 1.0], 'bootstrap': [True, False], 'bootstrap_features': [True, False], 'random_state': [42]}
# print(len(list(ParameterGrid(BC_Parameters))))