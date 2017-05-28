from magazine import magazine
import json


def main():
    with open('../data.json') as file:
        mgzSize = json.load(file)['magazine']
        mgz = magazine.Magazine(mgzSize['width'], mgzSize['height'])
    mgz.allocatePackages()
    mgz.displayPackages()
    print("")
    print("Packages left: " + str(len(mgz.packagesToPut)))
    print("Cost function(occupied area): " + str(mgz.calculateCost()))
    print("Heuristic function(area of packages left): " + str(mgz.heuristicFunction()))

if __name__ == "__main__":
    main()
