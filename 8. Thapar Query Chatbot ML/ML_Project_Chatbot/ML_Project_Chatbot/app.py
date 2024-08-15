from flask import Flask, request, jsonify, render_template
import torch
import torch.nn as nn
import os

# Define the neural network
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out

# Initialize the model
input_size = 10  # Example input size
hidden_size = 5  # Example hidden layer size
num_classes = 2  # Example number of output classes
model = NeuralNet(input_size, hidden_size, num_classes)

# Initialize Flask app
app = Flask(__name__, template_folder='template')

# Determine the absolute path to the index.html file
index_html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'index.html'))

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for model inference
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    inputs = torch.tensor(data['inputs'])
    outputs = model(inputs)
    _, predicted = torch.max(outputs.data, 1)
    return jsonify({'prediction': predicted.item()})

if __name__ == '__main__':
    app.run(debug=True)
