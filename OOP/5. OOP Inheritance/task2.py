import math

class TwoDVector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # Getter methods for x and y
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    # Setter methods for x and y
    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def add2DVectors(self, *vectors):
        for i in vectors:
            self.__x += i.__x
            self.__y += i.__y

    def print2DVector(self):
        if self.__y >= 0:
            y = "+ " + str(self.__y)
        else:
            y = str(self.__y)
        print(f"{self.__x}i {y}j")


class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z

    # Getter method for z
    def get_z(self):
        return self.__z

    # Setter method for z
    def set_z(self, z):
        self.__z = z

    def add3DVectors(self, *vectors):
        super().add2DVectors(*vectors)
        for vector in vectors:
            self.__z += vector.get_z()

    def multiplyScalar(self, scalar):
        self.set_x(self.get_x() * scalar)
        self.set_y(self.get_y() * scalar)
        self.__z *= scalar

    def calculateLength(self):
        return math.sqrt(self.get_x()**2 + self.get_y()**2 + self.__z**2)

    def print3DVector(self):
        x = self.get_x()
        y = self.get_y()
        z = self.__z
        y_sign = "+" if y >= 0 else ""
        z_sign = "+" if z >= 0 else ""
        print(f"{x}i {y_sign} {y}j {z_sign} {z}k")


# Test the classes
TwoDV1 = TwoDVector(5, 6)
TwoDV2 = TwoDVector(3, 7)
TwoDV3 = TwoDVector(1, 8)
print("===============")
TwoDV1.add2DVectors(TwoDV2, TwoDV3)
TwoDV1.print2DVector()
print("===============")
ThreeDV1 = ThreeDVector(5, 6, 1)
ThreeDV2 = ThreeDVector(1, 9, -7)
ThreeDV3 = ThreeDVector(8, 2, 4)
print("===============")
ThreeDV1.add3DVectors(ThreeDV2, ThreeDV3)
ThreeDV1.print3DVector()
print("===============")
ThreeDV1.multiplyScalar(3)
ThreeDV1.print3DVector()
print("===============")
print(ThreeDV1.calculateLength())