from flask import Flask, request, jsonify
from sklearn import datasets, model_selection, linear_model
import pickle

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def train_model():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Example: Using a Linear Regression model on dummy data
    X, y = datasets.make_regression(n_samples=100, n_features=1, noise=0.1)
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
    
    model = linear_model.LinearRegression()
    model.fit(X_train, y_train)
    
    # Serialize the model
    model_filename = 'model.pkl'
    with open(model_filename, 'wb') as f:
        pickle.dump(model, f)
    
    return jsonify({"message": "Model trained successfully!", "model_path": model_filename})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if 'features' not in data:
        return jsonify({"error": "No features provided"}), 400
    
    # Deserialize the model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    predictions = model.predict([data['features']])
    return jsonify({"predictions": predictions.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
