def main():
    name = input("What's you name? ")
    hello(name)

def hello(to="World"):
    print("Hello,", f"{to}!")

main()

