import math
class ArithmeticCalculations:
    def __init__(self):
        pass

    def factorial(self, number):
        if number < 0:
            raise ValueError("numbers lesser than 0 cannot have any factorial value")
        else:
            return f"the factorial of the number {number} is : {math.factorial(number)}"

    def sum(self, *args):
        sum_of_args = 0
        for arg in args:
            sum_of_args += arg
        return f"the sum of these numbers are : {sum_of_args}"

    def relatively_prime_numbers(self, nbr1, nbr2):
        # we call two numbers relatively prime when their only common dividor is 1
        if math.gcd(nbr1, nbr2) == 1:
            return f"the two numbers {nbr1} and {nbr2} are relatively prime numbers"
        else:
            return f"the two numbers {nbr1} and {nbr2} are not relatively prime numbers"

    def multiplication_table(self, integer):
        return f"{integer} x 1 = {integer} | {integer} x 2 = {integer*2} | {integer} x 3 = {integer*3} | {integer} x 4 = {integer*4}\n{integer} x 5 = {integer*5} | {integer} x 6 = {integer*6} | {integer} x 7 = {integer*7} | {integer} x 8 = {integer*8}\n{integer} x 9 = {integer*9} | {integer} x 10 = {integer*10}"

    def listDiv(self, nbr):
        dividors = []
        for i in range(1, nbr + 1):
            if nbr % i == 0:
                dividors.append(i)
        return f"the dividors of {nbr} is : {dividors}"

# testing the class
obj = ArithmeticCalculations()
print(obj.factorial(5))
print(obj.sum(1, 2, 3, 4))
print(obj.relatively_prime_numbers(9, 8))
print(obj.multiplication_table(3))
print(obj.listDiv(9))