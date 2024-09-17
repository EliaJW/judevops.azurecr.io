from BE.calculator_helper import CalculatorHelper
import pytest
class SetupClass():
   def setup_method(self):
       self.calculator = CalculatorHelper()
   def teardown_method(self):
       self.calculator = None


class TestCalculator(SetupClass): 
    def test_add(self) : 
        ##Arr
       #calculator = CalculatorHelper() 
       
        ## action 
        value = self.calculator.add(1, 1)
        assert value == 2

    def test_sub(self) : 
        ##Arr
       # calculator = CalculatorHelper()
        ## action
        value = self.calculator.subtract (1, 1)
        assert value == 0

    def test_mul(self) :
         ##Arr
        # calculator = CalculatorHelper()
         ## action
         value = self.calculator.multiply(3, 2)
         assert value == 6
    def test_div(self) :
        ##Arr
        #calculator = CalculatorHelper()
         ## action
         value = self.calculator.divide(6, 2)
         assert value == 3
    def test_div_zero(self):
        #calculator = CalculatorHelper()
        ## action
        with pytest.raises(ZeroDivisionError):
         1 / 0
   
@pytest.mark.parametrize("a,b, expected", 
         [(3,3, 6), 
         (3,-3, 0), 
         (6,9, 15)
 ])
def test_add_pytest(a,b, expected):
    calculator = CalculatorHelper()
    assert calculator.add(a,b) == expected