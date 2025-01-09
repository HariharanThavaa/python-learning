class Student:
    def __init__(self, name, house): 
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._house
    
    @property
    def name(self):
        return self._name

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house") 
        self._house = house
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")   
        self._name = name


def main():
    student = get_student()
    student._house = "Homeless"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()