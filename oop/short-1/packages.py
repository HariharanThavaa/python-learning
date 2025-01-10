class Package:
    def __init__(self, number, sender, receiver, weight):
        self.number = number
        self.sender = sender
        self.receiver = receiver
        self.weight = weight
    
    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.receiver}, {self.weight}kg"

def main():
    packages = [
        Package(number = 1, sender = "Alice", receiver = "Bob", weight = 10),
        Package(number = 2, sender = "Bob", receiver = "Charlie", weight = 5)
    ]
    for pkg in packages:
        print(pkg)

main()