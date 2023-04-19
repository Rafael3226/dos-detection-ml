import pickle

model = 'Any trained model'

# Save the model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Load the model from the file
with open('model.pkl', 'rb') as f:
    clf_loaded = pickle.load(f)
