class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        picture = ''
        if self.height <= 50 and self.width < 50:
            for points in range(self.height):
                widthpoints = ''
                for points in range(self.width):
                    widthpoints += '*'
                picture += widthpoints + '\n'
            return picture
        else:
            return "Too big for picture."
        
    def get_amount_inside(self, Shape):
        return self.get_area() // Shape.get_area()



class Square(Rectangle):
    def __init__(self, width=0):
        super().__init__(width)
        if self.height == 0:
            self.height = width
        elif self.width == 0:
            self.width = self.height
    
    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

rect = Rectangle(16,8)
sqr = Square(45)
print(rect, sqr)
print('--------------------------------')
print(rect.width, sqr.width)
print(rect.height, sqr.height)
print('--------------------------------')
print(rect.get_picture())
print(sqr.get_picture())
print('--------------------------------')
print(rect.get_amount_inside(sqr))