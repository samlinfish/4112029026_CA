from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas
from sklearn.preprocessing import LabelEncoder

data_frame = pandas.read_csv("healthcare_dataset.csv")

data_frame = data_frame.drop(['Name', 'Age', 'Date of Admission', 'Doctor', 'Hospital', 'Insurance Provider', 'Billing Amount', 'Room Number', 'Discharge Date'], axis = 1)

lc = LabelEncoder()
cols = ['Gender', 'Blood Type', 'Medical Condition', 'Admission Type', 'Medication', 'Test Results']
for i in cols:
    data_frame[i]=lc.fit_transform(data_frame[i])
data_frame.head()

y = data_frame['Test Results']
X = data_frame.drop(['Test Results'], axis = 1)

X_std = StandardScaler().fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_std, y, train_size = 0.2, random_state = 0)

my_favorite_tree = DecisionTreeClassifier()
my_favorite_tree.fit(X_train, y_train)

print(my_favorite_tree.score(X_test, y_test))