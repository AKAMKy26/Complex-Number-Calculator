import cmath

class Complexno:
    def __init__(self, complex_num):
        self.complex_num = complex_num

    @property
    def complex_num(self):
        return self._complex_num

    @complex_num.setter
    def complex_num(self, complex_num):
        complex_num = replace_fillers(complex_num)
        try:
            complex(complex_num)
        except ValueError:
            raise ValueError("Invalid Complex Number!")
        self._complex_num = complex(complex_num)

    @classmethod
    def get(cls, complex_num):
        first_complex_num = input("Enter Complex Number: ")
        return_list = [Complexno(first_complex_num)]
        multi_complex_num_op = ["add", "addition", "+","sub", "subtraction", "-","times", "multiplication", "*","div", "division", "/"]
        one_complex_num_op = ["magnitude", "abs","mag", "polar"]
        operation = input(f"Enter Operation:\nAddition(+)\nSubtraction(-)\nMultiplication(*)\nDivision(/)\nMagnitude(abs)\nPolar Conversion(polar)\n{"-" * 4}{": "}")
        operation = operation.lower()
        if operation in multi_complex_num_op:
            second_complex_num = input("Enter Second Complex Number: ")
            return_list.append(Complexno(second_complex_num))
        elif operation not in one_complex_num_op:
            raise ValueError("Invalid Operation!")
        return_list.append(operation)
        return return_list

    def __str__(self):
        return f"Answer: {self.complex_num.real} + {self.complex_num.img}i"

    def __add__(self, other):
        sum = self.complex_num + other.complex_num
        return Complexno(sum)

    def __sub__(self, other,):
        difference = self.complex_num - other.complex_num
        return Complexno(difference)
    
    def __mul__(self, other):
        product = self.complex_num * other.complex_num
        return Complexno(product)

    def __truediv__(self, other):
        quotient= self.complex_num / other.complex_num
        return Complexno(quotient)

    def __abs__(self):
        magnitude = abs(self.complex_num)
        return f"Answer: {magnitude}"

    def polar_convert(self):
        r , phi = cmath.polar(self.complex_num)
        return f"Answer: {r}, {phi} rad"


def result(first_number,operator, second_number):
    addition = ["add", "addition", "+"]
    subtraction = ["sub", "subtraction", "-"]
    multiplication = ["times", "multiplication", "*"]
    division = ["div", "division", "/"]
    magnitude = ["magnitude", "abs", "mag"]
    polar = ["polar"]
    if operator in addition:
        return first_number + second_number
    elif operator in subtraction:
        return first_number - second_number
    elif operator in multiplication:
        return first_number * second_number
    elif operator in division:
        return first_number / second_number
    elif operator in magnitude:
        return abs(first_number)
    elif operator in polar:
        return first_number.polar_convert()

def replace_fillers(complex):
    complex = complex.lower()
    return complex.replace(" ", "").replace("i", "j")