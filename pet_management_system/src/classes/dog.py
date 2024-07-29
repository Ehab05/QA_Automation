from pet_management_system.src.classes.pet import Pet


class Dog(Pet):
    def __init__(self, name, species, age, owner, vaccinated: bool, breed):
        super().__init__(name, species, age, owner, vaccinated)
        self.breed = breed

    @property
    def breed(self):
        return self.breed

    @breed.setter
    def breed(self, value):
        self.breed = value

    def __str__(self):
        return f"Name: {self.name}\nBreed: {self.breed}\nAge: {self.age}\nOwner: {self.owner}"

