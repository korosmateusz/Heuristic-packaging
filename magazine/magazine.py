from magazine import package
from resources import colors
from resources import node
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
        startingPackage = package.Package(0, 0) # non-existing package as algorithm starter
        startingPackage.xLocation = 0
        startingPackage.yLocation = 0
        self.packages.append(startingPackage)

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

    def putPackage(self, pack):
        for p in self.packagesToPut:
            if (p.width == pack.width and p.height == pack.height) \
                    or (p.width == pack.height and p.height == pack.width):
                self.packagesToPut.remove(p)
                break
        self.packages.append(pack)

    def allocatePackages(self):
        (best, target) = self.aStar()
        self.packages = best.packages
        self.packagesToPut = best.packagesToPut

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
        for centerPackage in self.packages:
            for packageToPut in self.packagesToPut:
                self.addPackageNeighboursToNeighbourhood(centerPackage, packageToPut, neighbourhood)
                packageToPut.rotate()
                self.addPackageNeighboursToNeighbourhood(centerPackage, packageToPut, neighbourhood)
        return neighbourhood

    def addPackageNeighboursToNeighbourhood(self, centerPackage, packageToPut, neighbourhood):
        xPossibilities = range(centerPackage.xLocation - packageToPut.width - 1,
                               centerPackage.xLocation + centerPackage.width + 2)
        yPossibilities = range(centerPackage.yLocation - packageToPut.height - 1,
                               centerPackage.yLocation + centerPackage.height + 2)
        for xToLocate in xPossibilities:
            for yToLocate in yPossibilities:
                if self.canBePut(packageToPut, xToLocate, yToLocate):
                    neighbour = packageToPut
                    neighbour.xLocation = xToLocate
                    neighbour.yLocation = yToLocate
                    neighbourhood.append(copy.deepcopy(neighbour))

    def aStar(self):
        log = node.Node()
        prevCosts = {}
        preceding = {}
        start = copy.deepcopy(self)
        prevCosts[start] = 0
        log.put(start, 0)
        best = (start, start.heuristicFunction())
        while not log.isEmpty():
            current = log.get()
            for neighbour in current.generateNeighbourhood():
                new = copy.deepcopy(current)
                new.putPackage(neighbour)
                cost = new.calculateCost()
                if new not in prevCosts or cost < prevCosts[new]:
                    prevCosts[new] = cost
                    heuristicFunction = new.heuristicFunction()
                    targetFunction = cost + heuristicFunction
                    log.put(new, targetFunction)
                    preceding[new] = current
                    if heuristicFunction == 0:
                        return new, targetFunction
                    if len(new.packages) > len(best[0].packages) \
                            or (targetFunction < best[1] and len(new.packages) == len(best[0].packages)):
                        best = (new, targetFunction)
        return best

    def calculateCost(self):
        return (self.getXCorner() + 1) * (self.getYCorner() + 1)

    def getXCorner(self):
        xCorner = 0
        for y in range(self.height-1, -1, -1):
            for x in range(self.width-1, -1, -1):
                for p in self.packages:
                    if p.isThere(x, y) and x > xCorner:
                        xCorner = x
        return xCorner

    def getYCorner(self):
        yCorner = 0
        for x in range(self.width-1, -1, -1):
            for y in range(self.height-1, -1, -1):
                for p in self.packages:
                    if p.isThere(x, y) and y > yCorner:
                        yCorner = y
        return yCorner

    def heuristicFunction(self):
        if not self.packagesToPut:
            return 0
        else:
            area = 0
            for p in self.packagesToPut:
                area += p.getArea()
            return area

    def __hash__(self):
        return hash((self.width, self.height, tuple(self.packages), tuple(self.packagesToPut)))

    def __eq__(self, other):
        if not (self.width, self.height) == (other.width, other.height):
            return False
        selfPackages = copy.deepcopy(self.packages)
        otherPackages = copy.deepcopy(other.packages)
        selfToRemove = []
        otherToRemove = []
        for pself in selfPackages:
            for pother in otherPackages:
                if pself == pother:
                    selfToRemove.append(pself)
                    otherToRemove.append(pother)
                    break
        for p in selfToRemove:
            selfPackages.remove(p)
        for p in otherToRemove:
            otherPackages.remove(p)
        if selfPackages or otherPackages:
            return False
        selfPackages = copy.deepcopy(self.packagesToPut)
        otherPackages = copy.deepcopy(other.packagesToPut)
        selfToRemove = []
        otherToRemove = []
        for pself in selfPackages:
            for pother in otherPackages:
                if pself == pother:
                    selfToRemove.append(pself)
                    otherToRemove.append(pother)
                    break
        for p in selfToRemove:
            selfPackages.remove(p)
        for p in otherToRemove:
            otherPackages.remove(p)
        if selfPackages or otherPackages:
            return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return True
