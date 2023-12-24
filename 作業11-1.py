from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score

digits = load_digits()
X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=45)

forest_classifier = RandomForestClassifier(random_state=45)
forest_classifier.fit(X_train, y_train)
forest_predictions = forest_classifier.predict(X_test)

forest_accuracy = accuracy_score(y_test, forest_predictions)
print("Random Forest Accuracy:", forest_accuracy)

adaboost_classifier = AdaBoostClassifier(random_state=45)
adaboost_classifier.fit(X_train, y_train)
adaboost_predictions = adaboost_classifier.predict(X_test)

adaboost_accuracy = accuracy_score(y_test, adaboost_predictions)
print("AdaBoost Accuracy:", adaboost_accuracy)
