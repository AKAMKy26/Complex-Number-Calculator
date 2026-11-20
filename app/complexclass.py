import cmath


class Complexno:
    def __init__(self, complex_num):
        self.complex_num = complex_num

    @property
    def complex_num(self):
        return self.complex_num

    @complex_num.setter
    def set_complex_num(self, complex_num):
        complex_num = replace_fillers(complex_num)
        if bool(complex(complex_num)) == False and not complex_num:
            raise ValueError("Invalid Complex Number!")
        self._complex_num = complex_num

    @classmethod
    def get(cls, complex_num):
        first_complex_num = input("Enter Complex Number: ")
        one_complex_num_op = ["add", "addition", "+","sub", "subtraction", "-","times", "multiplication", "*","div", "division", "/"]
        multi_complex_num_op = ["magnitude", "abs","mag", "polar"]
        operation = input("Enter Operation:\nAddition(+)\nSubtraction(-)\nMultiplication(*)\nDivision(/)\nMagnitude(abs)\nPolar Conversion(polar)\n", "-" * 4, ": ")
        operation = operation.lower()
        if operation in one_complex_num_op:
            second_complex_num = input("Enter Second Complex Number: ")
        elif operation not in multi_complex_num_op:
            raise ValueError("Invalid Operation!")
    
        return[Complexno(first_complex_num),operation, Complexno(second_complex_num)]

    def __add__(self, other):
        first_number = complex(self.complex_num)
        second_number = complex(other.complex_num)
        sum = first_number + second_number
        return Complexno(add_fillers(str(sum)))

    def __sub__(self, other,):
        first_number = complex(self.complex_num)
        second_number = complex(other.complex_num)
        difference = first_number - second_number
        return Complexno(add_fillers(str(difference)))
    
    def __mul__(self, other):
        first_number = complex(self.complex_num)
        second_number = complex(other.complex_num)
        product = first_number * second_number
        return Complexno(add_fillers(str(product)))

    def __truediv__(self, other):
            first_number = complex(self.complex_num)
            second_number = complex(other.complex_num)
            quotient = first_number / second_number
            return Complexno(add_fillers(str(quotient)))

    def __abs__(self):
        magnitude = abs(self.complex_num)
        return Complexno(add_fillers(str(magnitude)))

    def polar_convert(self):
        polar_form = cmath.polar(complex(self.complex_num))
        return Complexno(add_fillers(str(polar_form)))


    


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
        return Complexno.polar_convert(first_number)

def replace_fillers(complex):
    complex = complex.lower()
    return complex.replace(" ", "").replace("i", "j")

def add_fillers(complex):
    return complex.replace("", " ").replace("j","i")