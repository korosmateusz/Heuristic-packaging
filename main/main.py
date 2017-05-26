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

if __name__ == "__main__":
    main()
