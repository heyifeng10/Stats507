import xgboost
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import plot_importance
from matplotlib import pyplot
import pandas as pd
from sklearn.feature_selection import SelectFromModel
from numpy import sort
from sklearn.metrics import matthews_corrcoef
# Load Data
dataset = pd.read_csv('train_data_one_hot.csv')

# split data into X and y
X = dataset.drop(['target','appl_sbm_tm','id', 'birthday', 'phone', 'auth_time', 'id_card_x', 'is_hobby', 'id_card_y'], axis=1).to_numpy()
Y = dataset['target'].to_numpy()

# split data into training set and test set
seed = 7
test_size = 0.3
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
 
# fit the model
model = XGBClassifier()
model.fit(X_train, y_train)
 
# predict the test set
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
 
# evaluate the result
accuracy = accuracy_score(y_test, predictions)
mcc = matthews_corrcoef(y_test, predictions)
print("Accuracy: %.2f%%, MCC: %.2f%%" % (accuracy * 100.0, mcc * 100.0))
plot_importance(model)
pyplot.show()
