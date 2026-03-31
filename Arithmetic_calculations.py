import math
class ArithmeticCalculations:
    def __init__(self):
        pass

    @staticmethod
    def factorial(number):
        if number < 0:
            raise ValueError("numbers lesser than 0 cannot have any factorial value")
        else:
            return f"the factorial of the number {number} is : {math.factorial(number)}"

    @staticmethod
    def sum(*args):
        sum_of_args = 0
        for arg in args:
            sum_of_args += arg
        return f"the sum of these numbers are : {sum_of_args}"

    @staticmethod
    def relatively_prime_numbers(nbr1, nbr2):
        # we call two numbers relatively prime when their only common dividor is 1
        if math.gcd(nbr1, nbr2) == 1:
            return f"the two numbers {nbr1} and {nbr2} are relatively prime numbers"
        else:
            return f"the two numbers {nbr1} and {nbr2} are not relatively prime numbers"

    @staticmethod
    def is_even(number):
        if number % 2 == 0:
            return f"the number {number} is even"
        else:
            return f"the number {number} is not even"

    @staticmethod
    def list_div(nbr):
        dividors = []
        for i in range(1, nbr + 1):
            if nbr % i == 0:
                dividors.append(i)
        if len(dividors) == 1:
            return f"the dividors of {nbr} is : {dividors}"
        else:
            return f"the dividors of {nbr} are : {dividors}"

# testing the class
obj = ArithmeticCalculations()
print(obj.factorial(5))
print(obj.sum(1, 2, 3, 4))
print(obj.relatively_prime_numbers(9, 8))
print(obj.is_even(3))
print(obj.list_div(18))