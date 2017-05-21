from magazine import package
from resources import colors
import sys

class Magazine:
    width = 0
    height = 0
    packages = []

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getPackages(self):
        self.packages.append(package.Package(2, 3))
        self.packages.append(package.Package(1, 4))
        self.packages.append(package.Package(5, 1))

    def allocatePackages(self):
        self.packages[0].xLocation = 1
        self.packages[0].yLocation = 1
        self.packages[1].xLocation = 5
        self.packages[1].yLocation = 1
        self.packages[2].xLocation = 1
        self.packages[2].yLocation = 7

    def printPackages(self):
        for y in range(0, 10):
            for x in range(0, 7):
                wasPrinted = False
                for p in self.packages:
                    if p.isThere(x, y):
                        sys.stdout.write(colors.Colors.GREEN + "0" + colors.Colors.ENDC)
                        wasPrinted = True
                        break
                if not wasPrinted:
                    sys.stdout.write(colors.Colors.RED + "0" + colors.Colors.ENDC)
            print("")
