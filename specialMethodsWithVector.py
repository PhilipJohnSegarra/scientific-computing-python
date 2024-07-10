class R2Vector:
    def __init__(self, *, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)            
        return NotImplemented

    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other

class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z
        
    def cross(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        
        return self.__class__(**kwargs)
    
# Explanation about special methods:
# Special methods in Python, also known as magic or dunder methods (due to their double underscore prefix and suffix),
# allow objects to emulate the behavior of built-in types and interact with operators or built-in functions.
# In this code:
# - __init__ initializes vector components.
# - __str__ and __repr__ provide string representations for printing and debugging.
# - __add__, __sub__, __mul__ define vector addition, subtraction, and scalar/dot product multiplication.
# - Comparison methods (__eq__, __ne__, __lt__, __gt__, __le__, __ge__) allow comparison based on vector norms.
# These methods make instances of R2Vector and R3Vector behave like mathematical vectors, supporting typical operations.

# Discussion about vectors and their formulas:
# Vectors in mathematics and physics represent quantities with both magnitude and direction. In 2D and 3D,
# vectors are commonly represented by coordinates (x, y) and (x, y, z) respectively. Key formulas include:
# - Norm (magnitude): ||v|| = sqrt(x^2 + y^2) for 2D, and ||v|| = sqrt(x^2 + y^2 + z^2) for 3D.
# - Addition: v + w = (v_x + w_x, v_y + w_y) for 2D, and similarly for 3D.
# - Subtraction: v - w = (v_x - w_x, v_y - w_y) for 2D, and similarly for 3D.
# - Scalar (dot) product: v ⋅ w = v_x * w_x + v_y * w_y for 2D, and v ⋅ w = v_x * w_x + v_y * w_y + v_z * w_z for 3D.
# - Cross product (specific to 3D vectors): v × w = (v_y * w_z - v_z * w_y, v_z * w_x - v_x * w_z, v_x * w_y - v_y * w_x).

# Using these formulas, vectors can represent physical quantities such as forces, velocities, or positions,
# and their operations are essential in physics, computer graphics, and many other fields.

    
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v5 = v1 * v2
print(f'v1 * v2 = {v5}')
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')