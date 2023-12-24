from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score

digits = load_digits()
X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

forest_classifier = RandomForestClassifier()
forest_classifier.fit(X_train, y_train)
forest_predictions = forest_classifier.predict(X_test)

print("Forest:", accuracy_score(y_test, forest_predictions))

adaboost_classifier = AdaBoostClassifier()
adaboost_classifier.fit(X_train, y_train)

adaboost_accuracy = accuracy_score(y_test, adaboost_classifier.predict(X_test))
print("AdaBoost:", adaboost_accuracy)
