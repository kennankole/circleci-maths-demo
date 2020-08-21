'''
Unit tests for the calculator library
'''

import caluculator


class TestCalculator:

    def test_addition(self):
        assert 4 == caluculator.add(2, 2)

    def test_substract(self):
        assert 2 == caluculator.substract(4, 2)
