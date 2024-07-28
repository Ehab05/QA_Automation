from pet_management_system.logic.pet import Pet


class Cat(Pet):
    def __init__(self, name, species, age, owner, vaccinated: bool, indoor: bool):
        super().__init__(name, species, age, owner, vaccinated)
        self.indoor = indoor

    @property
    def indoor(self):
        return self.indoor

    @indoor.setter
    def indoor(self, value):
        self.indoor = value

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}indoor: {self.indoor}\n\nOwner: {self.owner}"
