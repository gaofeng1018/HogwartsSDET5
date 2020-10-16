import pytest

from pythoncode.calculator import Calculator

# def test_a():
#     print("test case a")

class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect',[
        [1, 1, 2], [100, 100, 200], [0.1, 0.3, 0.4], [-1, -1, -2], [1, 0, 1]
    ], ids = ['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case'])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    def test_add1(self):
        # calc = Calculator()
        try:
            result = self.calc.add(1, '1')
        except Exception as e:
            print("type error", e)
    # def test_add2(self):
    #     # calc = Calculator()
    #     result = self.calc.add(100,100)
    #     assert result == 200
    #
    # def test_add3(self):
    #     # calc = Calculator()
    #     result = self.calc.add(0.1,0.3)
    #     assert result == 0.4
    #
