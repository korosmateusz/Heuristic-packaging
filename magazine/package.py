from resources import colors
import sys


class Package:
    width = 0
    height = 0
    xLocation = 0
    yLocation = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def isThere(self, x, y):
        if self.xLocation <= x < self.xLocation + self.width and self.yLocation <= y < self.yLocation + self.height:
            return True
        else:
            return False

    def print(self, x, y):
        if self.xLocation <= x < self.xLocation+self.width and self.yLocation <= y < self.yLocation+self.height:
            sys.stdout.write(colors.Colors.GREEN + "0" + colors.Colors.ENDC)
        else:
            sys.stdout.write(colors.Colors.RED + "0" + colors.Colors.ENDC)
