from python.calc import Calc
import pytest


class TestCalc:
    @pytest.mark.parametrize('data1,data2,answer',[(1,1,2),(1,-1,0),(-1,-2,-3),(0.1,-5,-4.9),(10000000,0.1,10000000.1)])
    def test_add(self,data1,data2,answer):
        self.calc = Calc()
        resault = self.calc.Add(data1, data2)
        assert resault == answer

    @pytest.mark.parametrize('data1,data2,answer', [(1,2,0.5),(-1,-5,0.2),(0,9,0),(1,1000000,0.000001)])
    def test_div(self,data1,data2,answer):
        self.calc = Calc()
        resault = self.calc.Div(data1,data2)
        assert resault == answer

