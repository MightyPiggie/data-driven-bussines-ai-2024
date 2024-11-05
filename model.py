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
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from joblib import dump, load
import os.path
import warnings
warnings.simplefilter('ignore')

models = {
    "BaggingClassifier": Pipeline([('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform="pandas")), ('bc', BaggingClassifier())]),
    "RandomForestClassifier": Pipeline([('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform="pandas")), ('RFC', RandomForestClassifier())]),
    "ExtraTreesClassifier": Pipeline([('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform="pandas")), ('ETC', ExtraTreesClassifier())]),
    "GaussianNB": Pipeline([('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform="pandas")), ('GNB', GaussianNB())]),
    "NearestNeighborsClassifier": Pipeline([('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform="pandas")), ('KNC', KNeighborsClassifier())]),
    "MLPClassifier": Pipeline([('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform="pandas")), ('MLPC', MLPClassifier())]),
    "LinearTreeClassifier": Pipeline([('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform="pandas")), ('LTC', LinearTreeClassifier(base_estimator=RidgeClassifier()))]),
    "LinearForestClassifier": Pipeline([('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform="pandas")), ('LFC', OneVsRestClassifier(LinearForestClassifier(Ridge(), max_features="sqrt")))]),
    "LinearBoostClassifier": Pipeline([('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform="pandas")), ('LBC', LinearBoostClassifier(base_estimator=RidgeClassifier()))]),
    "VotingClassifier": Pipeline([('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform="pandas")), ('VC', VotingClassifier(estimators=[("BC", BaggingClassifier()), ("RFC", RandomForestClassifier()),("LFC", OneVsRestClassifier(LinearForestClassifier(Ridge(), max_features="sqrt")))], voting="soft"))]),
    "DecisionTreeClassifier": Pipeline([('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore').set_output(transform="pandas")), ('DTC', DecisionTreeClassifier())])
}

def train_models(models, X_train, X_test, y_train, y_test):
    print("Training models...")
    for name, model in models.items():
        if not os.path.isfile(f"models/{name}.joblib"):
            model.fit(X_train, y_train)
            dump(model, f"models/{name}.joblib")
        else:
            model = load(f"models/{name}.joblib")
        score = model.score(X_test, y_test)
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(X_test)
            log_loss_proba = log_loss(y_test, proba)
            print(f"{name} - {score} - {log_loss_proba}")
        else:
            print(f"{name} - {score}")

# BC_Parameters = {'estimator': [LinearTreeClassifier(base_estimator=RidgeClassifier()), OneVsRestClassifier(LinearForestClassifier(Ridge(), max_features="sqrt")), RandomForestClassifier(), ExtraTreesClassifier(), MLPClassifier(), KNeighborsClassifier(), GaussianNB()], 'n_estimators': [10, 50, 100], 'max_samples': [0.5, 1.0], 'max_features': [0.5, 1.0], 'bootstrap': [True, False], 'bootstrap_features': [True, False], 'random_state': [42]}
# print(len(list(ParameterGrid(BC_Parameters))))