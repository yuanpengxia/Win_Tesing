import pytest


@pytest.fixture()
class Calc:
    def Add(self, a, b):
        return a + b

    def Div(self, a, b):
        return a / b

    def Sub(self, a, b):
        return a - b

    def Mul(self, a, b):
        return a * b
