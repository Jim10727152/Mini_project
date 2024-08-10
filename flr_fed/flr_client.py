import argparse
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers, models
import flwr as fl  # Federated learning architecture

# Parse command line arguments
parser = argparse.ArgumentParser(description="Train a model with federated learning on a specified CSV file.")
parser.add_argument('--csv', type=str, required=True, help='Path to the CSV file.')
args = parser.parse_args()

# Load data
data = pd.read_csv(args.csv)

# Assuming 'label' column is the target
x = data.drop(columns=['label']).values
y = data['label'].values

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Standardize the training set
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)

# Apply the training set's mean and std to standardize the testing set
x_test = scaler.transform(x_test)

# Continue with the model training process
num_features = x_train.shape[1]
input_shape = (num_features,)

model = models.Sequential([
    tf.keras.Input(shape=input_shape),
    layers.Dense(128, activation="relu"),
    layers.Dense(64, activation="relu"),
    layers.Dropout(0.5),
    layers.Dense(1, activation="sigmoid"),  # Use sigmoid to output a single value (0 or 1)
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

class CsvClient(fl.client.NumPyClient):

    def get_parameters(self, config):
        return model.get_weights()

    def fit(self, parameters, config):
        model.set_weights(parameters)
        model.fit(x_train, y_train, epochs=3, batch_size=64)
        return model.get_weights(), len(x_train), {}

    def evaluate(self, parameters, config):
        model.set_weights(parameters)
        loss, accuracy = model.evaluate(x_test, y_test)
        return loss, len(x_test), {"accuracy": accuracy}

fl.client.start_client(server_address="localhost:8080", client=CsvClient().to_client())
