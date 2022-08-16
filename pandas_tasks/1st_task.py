class rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        calc_area = self.x * self.y
        return calc_area


v1 = rectangle(2, 3)
print(v1.area())


