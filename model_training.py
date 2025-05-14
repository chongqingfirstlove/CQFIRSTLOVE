import numpy as np
from sklearn.neural_network import MLPClassifier

class AdaboostBP:
    def __init__(self, n_estimators=10):
        self.n_estimators = n_estimators
        self.estimators = []
        self.alphas = []

    def fit(self, X, y):
        # 确保 y 是 numpy 数组
        y = np.array(y)
        n_samples = X.shape[0]
        D = np.ones(n_samples) / n_samples  # 初始化样本权重

        for _ in range(self.n_estimators):
            # 创建BP神经网络分类器
            clf = MLPClassifier(hidden_layer_sizes=(10,), max_iter=200)

            # 按照样本权重进行采样
            indices = np.random.choice(n_samples, size=n_samples, replace=True, p=D)
            X_sampled = X[indices]
            y_sampled = y[indices]

            clf.fit(X_sampled, y_sampled)

            y_pred = clf.predict(X)
            error = np.sum(D * (y_pred != y))

            alpha = 0.5 * np.log((1 - error) / error)

            D = D * np.exp(-alpha * y * y_pred)
            D = D / np.sum(D)

            self.estimators.append(clf)
            self.alphas.append(alpha)

    def predict_proba(self, X):
        n_samples = X.shape[0]
        scores = np.zeros(n_samples)

        for alpha, clf in zip(self.alphas, self.estimators):
            scores += alpha * clf.predict(X)

        proba = 1 / (1 + np.exp(-scores))
        return proba