from magazine import package
from resources import colors
import sys
import json


class Magazine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.packages = []
        self.getPackages()

    def getPackages(self):
        with open('../data.json') as file:
            packs = json.load(file)['packages']
            for pack in packs:
                self.packages.append(package.Package(pack['width'], pack['height']))

    def allocatePackages(self):
        self.packages[0].xLocation = 1
        self.packages[0].yLocation = 1
        self.packages[1].xLocation = 5
        self.packages[1].yLocation = 1
        self.packages[2].xLocation = 1
        self.packages[2].yLocation = 7

    def printPackages(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                wasPrinted = False
                for p in self.packages:
                    if p.isThere(x, y):
                        sys.stdout.write(colors.Colors.GREEN + "0" + colors.Colors.NORMAL)
                        wasPrinted = True
                        break
                if not wasPrinted:
                    sys.stdout.write(colors.Colors.RED + "0" + colors.Colors.NORMAL)
            print("")
