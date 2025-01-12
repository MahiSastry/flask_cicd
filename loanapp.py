from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Loan Approval System"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    amount = data.get('loan_amount', 0)
    # Simple logic: approve loans <= 100000
    result = 'approved' if amount <= 100000 else 'rejected'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)