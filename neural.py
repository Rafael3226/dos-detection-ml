from tensorflow import keras
import pandas as pd
import pickle
from keras.models import Sequential
from keras.layers import Dense

# create a sequential model
model = Sequential()

# add layers to the model
model.add(Dense(64, input_dim=11, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the model
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])


# Load the training and test datasets
train_df = pd.read_csv('./processed/training.csv')
test_df = pd.read_csv('./processed/test.csv')

# Select the features and target variable
features = train_df.drop('is attack', axis=1)
target = train_df['is attack']

# train the model
model.fit(features.values, target.values, epochs=10, batch_size=32)

# export the model
# Save the model to a file
with open('./models/neural_network.pkl', 'wb') as file:
    pickle.dump(model, file)

# Evaluate the model on the test data
test_features = test_df.drop('is attack', axis=1)
test_target = test_df['is attack']
accuracy = model.evaluate(test_features, test_target, batch_size=32)

print("Accuracy on test data:", accuracy)
