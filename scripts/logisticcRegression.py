import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the training and test datasets
train_df = pd.read_csv('training.csv')
test_df = pd.read_csv('test.csv')

# Split the datasets into features (X) and target (y)
X_train = train_df.drop('is attack', axis=1)
y_train = train_df['is attack']
X_test = test_df.drop('is attack', axis=1)
y_test = test_df['is attack']

# Train a logistic regression model
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

# Test the model on the test dataset
y_pred = lr_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy score
print("Accuracy:", accuracy)