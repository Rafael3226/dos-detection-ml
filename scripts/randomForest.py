import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the training and test datasets
train_df = pd.read_csv('training.csv')
test_df = pd.read_csv('test.csv')

# Split the datasets into input features (X) and target variable (y)
X_train = train_df.drop('is attack', axis=1)
y_train = train_df['is attack']
X_test = test_df.drop('is attack', axis=1)
y_test = test_df['is attack']

# Train a random forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions on the test dataset
y_pred = rf_model.predict(X_test)

# Evaluate the model's accuracy on the test dataset
accuracy = accuracy_score(y_test, y_pred)
print("Random Forest Accuracy: {:.2f}%".format(accuracy*100))