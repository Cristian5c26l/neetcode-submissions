import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length: int, width: int = None):
        if width is None:
            circle_area = math.pi * (length ** 2)
            return round(circle_area, 2)

        rectangle_area = length * width
        return rectangle_area

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
