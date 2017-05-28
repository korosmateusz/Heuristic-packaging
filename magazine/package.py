class Package:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.xLocation = -1
        self.yLocation = -1

    def isThere(self, x, y):
        if self.xLocation <= x < self.xLocation + self.width and self.yLocation <= y < self.yLocation + self.height:
            return True
        else:
            return False

    def getArea(self):
        return self.width * self.height

    def rotate(self):
        self.width, self.height = self.height, self.width

    def __hash__(self):
        return hash((self.width, self.height, self.xLocation, self.yLocation))

    def __eq__(self, other):
        if ((self.width == other.width and self.height == other.height)
            or (self.width == other.height and self.height == other.width)) \
          and self.xLocation == other.xLocation and self.yLocation == other.yLocation:
            return True
        return False

    def __ne__(self, other):
        return not (self == other)

