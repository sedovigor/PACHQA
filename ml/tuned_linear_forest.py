import os
from sklearn.base import (BaseEstimator,
                          TransformerMixin)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold

from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SequentialFeatureSelector as SFS

from sklearn.linear_model import LinearRegression as LinReg
from lineartree import LinearForestRegressor as LFR

_fs_params = {
    'min_samples_leaf': 3,
    'n_estimators': 50,
    'max_depth': None,
    'max_features': None,
}

_hp_grid = {
    'min_samples_leaf': [3, 5, 7],
    'n_estimators': [100, 200, 300, 400, 500, 750, 1000],
    'max_features': ['sqrt', None],
}


class TunedLinearForest(BaseEstimator, TransformerMixin):
    def __init__(self, cv=5, random_state=0, max_threads=None):
        self.cv = cv
        self.random_state = random_state
        self.model = None
        self.selected_features_ = None
        self.best_params_ = None
        self.max_threads = max_threads or os.cpu_count()

    def fit(self, X, y):
        self.model = LFR(LinReg(),
                         max_depth=None,
                         random_state=self.random_state,
                         n_jobs=self.max_threads//self.cv)

        # Feature selection
        X = self.select_features(X, y)

        # Hyperparameter tuning
        self.best_params_ = self.hyperparameter_search(X, y)

        # Fit the final model
        self.model.set_params(**self.best_params_)
        self.model.fit(X, y)

    def predict(self, X):
        if not hasattr(self, 'pipe'):
            raise RuntimeError("Model not fitted yet. Call 'fit' first.")
        X = self.pipe.transform(X)
        return self.model.predict(X)

    def select_features(self, X, y):
        """Scale features and select them using a SequentialFeatureSelector."""
        self.pipe = Pipeline([
            ('selector_0', VarianceThreshold()),
            ('scaler', StandardScaler()),
            ('selector_1', SFS(
                self.model.set_params(**_fs_params),
                cv=self.cv,
                n_jobs=self.cv,
                scoring='r2',
                tol=1e-6)
            ),
        ])
        self.pipe.fit(X, y)

        # Get feature names if X is instance of pd.DataFrame
        if hasattr(X, 'columns'):
            sf = X.columns[self.pipe.named_steps['selector_0'].get_support()]
            sf = sf[self.pipe.named_steps['selector_1'].get_support()]
            self.selected_features_ = sf
        return self.pipe.transform(X)

    def hyperparameter_search(self, X, y):
        """Perform grid search for hyperparameter tuning."""
        self.searcher = GridSearchCV(
            self.model,
            _hp_grid,
            scoring='r2',
            cv=self.cv,
            n_jobs=self.cv
        )
        self.searcher.fit(X, y)
        return self.searcher.best_params_