class Package:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.xLocation = 0
        self.yLocation = 0

    def isThere(self, x, y):
        if self.xLocation <= x < self.xLocation + self.width and self.yLocation <= y < self.yLocation + self.height:
            return True
        else:
            return False
