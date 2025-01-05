def main():
    name = get_name()
    house = get_address()
    print(f"{name} from {house}")

def get_name():
    name = input("Name: ")
    return name

def get_address():
    house = input("House: ")
    return house

if __name__ == "__main__":
    main()