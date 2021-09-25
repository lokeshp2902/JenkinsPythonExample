class Addition:

    def add(self, operand1, operand2):
        return operand1 + operand2

    def addAll(self, numbers):
        sum = 0
        for number in numbers:
            sum = sum + number
        return sum

        