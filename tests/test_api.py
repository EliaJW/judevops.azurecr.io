import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate 
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models.result_response import ResultResponse 

class TestCalcApi ():
    def test_clculate(self):

       url = 'http://localhost:5000/calculate'
       payload = {
         "operation": "add",
          "operand1": 1,
         "operand2": 1
       }
       ###s
       response = requests.post(url, json=payload)

       assert response.status_code == 200

       data = response.json()

       assert data['result'] == 2

    def test_auto_code(self) : 
      client = Client("http://localhost:5000/")
      calculation = Calculation(operation=Opertions.ADD, operand1=1, operand2=1)
      response: ResultResponse = calculate.sync(client=client, body=calculation)
      assert response.result == 2 