from magazine import package
from resources import colors
from random import randint
import sys
import json
import copy


class Magazine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.packages = []
        self.packagesToPut = []
        self.getPackages()

    def getPackages(self):
        with open('../data.json') as file:
            packs = json.load(file)['packages']
            for p in packs:
                self.packagesToPut.append(package.Package(p['width'], p['height']))

    def displayPackages(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                wasPrinted = False
                for p in self.packages:
                    if p.isThere(x, y):
                        sys.stdout.write(colors.Colors.GREEN + "1" + colors.Colors.NORMAL)
                        wasPrinted = True
                        break
                if not wasPrinted:
                    sys.stdout.write(colors.Colors.RED + "0" + colors.Colors.NORMAL)
            print("")

    def putPackage(self, pack, x, y):
        for p in self.packagesToPut:
            if (p.width == pack.width and p.height == pack.height) or (p.width == pack.height and p.height == pack.width):
                self.packagesToPut.remove(p)
                break
        pack.xLocation = x
        pack.yLocation = y
        self.packages.append(pack)


    def allocatePackages(self):
        self.putPackage(self.packagesToPut[0], 0, 0)
        while True:
            neighbourhood = self.generateNeighbourhood()
            if len(neighbourhood) > 0:
                rand = randint(0, len(neighbourhood)-1)
                self.putPackage(neighbourhood[rand], neighbourhood[rand].xLocation, neighbourhood[rand].yLocation)
            else:
                break

    def canBePut(self, pack, xToPut, yToPut):
        if xToPut < 0 or yToPut < 0 or xToPut + pack.width > self.width or yToPut + pack.height > self.height:
            return False
        for x in range(xToPut - 1, xToPut + pack.width + 1):
            for y in range(yToPut - 1, yToPut + pack.height + 1):
                for p in self.packages:
                    if x < 0 or y < 0:
                        break
                    if p.isThere(x, y):
                        return False
        return True

    def generateNeighbourhood(self):
        neighbourhood = []
        for pack in self.packages:
            for packToPut in self.packagesToPut:
                xPossibilities = range(pack.xLocation - packToPut.width - 1, pack.xLocation + pack.width + 2)
                yPossibilities = range(pack.yLocation - packToPut.height - 1, pack.yLocation + pack.height + 2)
                for xToLocate in xPossibilities:
                    for yToLocate in yPossibilities:
                        if self.canBePut(packToPut, xToLocate, yToLocate):
                            neighbour = packToPut
                            neighbour.xLocation = xToLocate
                            neighbour.yLocation = yToLocate
                            neighbourhood.append(copy.deepcopy(neighbour))
        return neighbourhood
