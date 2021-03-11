"""
Unit testing calc
"""


import calculator


class TestCalc:

    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_sub(self):
        assert 2 == calculator.sub(3, 1)
