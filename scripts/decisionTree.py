import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the training and test datasets
train_df = pd.read_csv('training.csv')
test_df = pd.read_csv('test.csv')

# Select the features and target variable
features = train_df.drop('is attack', axis=1)
target = train_df['is attack']

# Train the decision tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(features, target)

# Evaluate the model on the test data
test_features = test_df.drop('is attack', axis=1)
test_target = test_df['is attack']
predictions = model.predict(test_features)
accuracy = accuracy_score(test_target, predictions)

print("Accuracy on test data:", accuracy)