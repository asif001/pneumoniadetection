from flask import Flask, request
from flask_cors import CORS
from model.predict import predict_pneumonia

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def predict():
    data = request.files["file"]
    if data is None:
        return 'Nothing'
    else:
        print("Got it")
        result = predict_pneumonia(data)
        return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
