from magazine import magazine


def main():
    mgz = magazine.Magazine(7, 10)
    mgz.getPackages()
    mgz.allocatePackages()
    mgz.printPackages()

if __name__ == "__main__":
    main()
