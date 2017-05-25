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
