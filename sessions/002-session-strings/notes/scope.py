#! /usr/bin/env python3

# g e l ??

x = 100

print(f"global x is: {x}")

def add_5(x):
    print("What is the current value of x as argument of add_5?")
    input("> ")
    print(f"add_5 argument x is: {x}")
    x = 0
    x = x + 5
    print("What is the current value of x after adding 5, but before returning?")
    input("> ")
    print(f"x in add_5 is: {x}")
    return x

def main():
    x = 20
    print(f"x in main() is: {x}")
    print("calling add_5...")
    def add_5(x):
        print("What is the current value of x as argument of add_5?")
        input("> ")
        print(f"add_5 argument x is: {x}")
        x = 0
        x = x + 5
        print("What is the current value of x after adding 5, but before returning?")
        input("> ")
        print(f"x in add_5 is: {x}")
        return x

    y = add_5(x)
    print("What is the return value of add_5?")
    input("> ")
    print(f"x returned from add_5 is: {y}")
    # x = 50
    # print("calling add_5 again with new x...")
    print("What is the value of x in main after add_5?")
    input("> ")
    print(f"x at the end of main() is: {x}")


if __name__ == '__main__':
    x = 10
    print(f"x before main() is: {x}")
    main()
    print("What is the value of x after main()?")
    input("> ")
    print(f"x after main() is {x}")