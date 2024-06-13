class Task2:
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    def power(n1, n2):
        return n1 ** n2

    def remainder(n1, n2):
        return n1 // n2

    def menuDisplay():
        print("select the desired operation:-")
        print("1: +")
        print("2: -")
        print("3: *")
        print("4: /")
        print("5: ** (power)")
        print("6: // (remainder)")
        print("7: exit")

    def main():
        while True:
            Task2.menuDisplay()
            chosen = int(input("select operations from 1 - 7: "))

            if chosen == 7:
                print("exiting")
                break

            n1 = int(input("choose your 1st number: "))
            n2 = int(input("choose your 2nd number: "))

            if chosen == 1:
                print(Task2.add(n1, n2))
            elif chosen == 2:
                print(Task2.subtract(n1, n2))
            elif chosen == 3:
                print(Task2.multiply(n1, n2))
            elif chosen == 4:
                print(Task2.divide(n1, n2))
            elif chosen == 5:
                print(Task2.power(n1, n2))
            else:
                print(Task2.remainder(n1, n2))

if __name__ == "__main__":
    Task2.main()
