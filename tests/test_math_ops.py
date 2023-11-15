import pytest
import random


class TestMathOps:

    def setup_class(cls):
        cls.number1 = random.randint(0, 100)
        cls.number2 = random.randint(0, 100)

    def teardown_class(cls):
        print("teardown_class called once for the class")
        del cls.number1
        del cls.number2

    def test_add(self):
        sum = self.number1 + self.number2
        assert sum < 100

    def test_subtract(self):
        assert self.number1-self.number2 != 0

    def test_multiply(self):
        assert self.number1*self.number2 != 0

    def test_divide(self):
        assert self.number1/self.number2 != 0

    def test_pytest_fail(self):
        if self.number1 == 10:
            pytest.fail("a should not be 10")
