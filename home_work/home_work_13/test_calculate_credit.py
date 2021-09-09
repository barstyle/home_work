from unittest import TestCase, main
from testing_example import calculate_credit


class CalculatorCreditTest(TestCase):
    def test_calc(self):
        self.assertEqual(calculate_credit(20000, 0.12, 36), 664.29)

    def test_loan_is_null(self):
        self.assertEqual(calculate_credit(0, 0.1, 36), 'Зачем вам 0 деняк в кредит?')

    def test_symbol(self):
        self.assertEqual(calculate_credit('+', 0, 36), 'Значения должны быть числами')

    def test_percent_is_null(self):
        self.assertEqual(calculate_credit(1000, 0, 36), 'Значения не должны быть равны нулю')

    def test_term_is_null(self):
        self.assertEqual(calculate_credit(1000, 0.1, 0), 'Значения не должны быть равны нулю')

    def test_minus(self):
        self.assertEqual(calculate_credit(-1000, 0.12, 36), 'Значения не должны быть отрицательными')

    def test_term(self):
        self.assertEqual(calculate_credit(100, 0.12, 1202), 'Срок кредита не должен превышать 100 лет')

if __name__ == "__main__":
    main()