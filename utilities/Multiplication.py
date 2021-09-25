class Multiplication:

    def mul(self, operand1, operand2):
        return operand1 * operand2

    def mulNum(self, numbers):
        multiply = 1
        for number in numbers:
            multiply = multiply * number
        return multiply