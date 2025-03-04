from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandler:
  def average(self, numbers: List[float]) -> float:
    return 1
  
class MockDriverHandlerError:
  def average(self, numbers: List[float]) -> float:
    return 0
  
def test_calculate_average_with_body_error():
  mock_request = MockRequest(body={ "numberssss": [] })
  calculator_4 = Calculator4(MockDriverHandler())

  with raises(Exception) as excinfo:
    calculator_4.calculate(mock_request)

  assert str(excinfo.value) == "body mal formatado!"
  
def test_calculate_average_with_empty_body_error():
  mock_request = MockRequest(body={ "numbers": [] })
  calculator_4 = Calculator4(MockDriverHandler())

  with raises(Exception) as excinfo:
    calculator_4.calculate(mock_request)

  assert str(excinfo.value) == "Não foi informado nenhum número para o cálculo!"

def test_calculate():
  mock_request = MockRequest(body={ "numbers": [1, 1, 1, 1, 1] })
  calculator_4 = Calculator4(MockDriverHandler())
  
  response = calculator_4.calculate(mock_request)

  assert response == {'data': {'Calculator': 4, 'value': 1, 'Success': True}}