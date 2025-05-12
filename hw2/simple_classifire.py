
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

class SimpleClassifier:
    def __init__(self, max_iter=100):
        self.model = LogisticRegression(max_iter=max_iter)
        self.scaler = StandardScaler()

    def train(self, X_train, y_train):
        X_scaled = self.scaler.fit_transform(X_train)
        self.model.fit(X_scaled, y_train)

    def predict(self, X_test):
        X_scaled = self.scaler.transform(X_test)
        return self.model.predict(X_scaled)

    def evaluate(self, X_test, y_test):
        X_scaled = self.scaler.transform(X_test)
        return self.model.score(X_scaled, y_test)