"""
Unit testing calc
"""


import calculator


class testCalc:
    def test_add(self):
        assert 5 == calc.add(1, 4)

    def test_sub(self):
        assert 2 == calc.add(3, 1)
