import pytest
from loanapp import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Welcome to Loan Approval System"

def test_predict_approved(client):
    test_data = {'loan_amount': 50000}
    response = client.post('/predict', json=test_data)
    assert response.status_code == 200
    assert response.json['result'] == 'approved'

def test_predict_rejected(client):
    test_data = {'loan_amount': 150000}
    response = client.post('/predict', json=test_data)
    assert response.status_code == 200
    assert response.json['result'] == 'rejected'