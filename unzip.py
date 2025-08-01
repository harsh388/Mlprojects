import gzip
import pickle

# Unzip and load the model
model_file_path = "model.pkl.gz"
with gzip.open(model_file_path, "rb") as f:
    loaded_model = pickle.load(f)

print("Loaded model type:", type(loaded_model))

# Unzip and load the preprocessor
preprocessor_file_path = "preprocessor.pkl.gz"
with gzip.open(preprocessor_file_path, "rb") as f:
    loaded_preprocessor = pickle.load(f)

print("Loaded preprocessor type:", type(loaded_preprocessor))