from pet_management_system.file_handler import FileHandler
from pet_management_system.src.classes.utils import Utils


class Pet:
    def __init__(self, name, species, age, owner, vaccinated: bool):
        self._file_path = Utils().setup_environment(__file__, "../../pet_store_management.json", "../../")
        self._pet_store_management = FileHandler(self._file_path, 'r+')
        self._name = name
        self._species = species
        self._age = age
        self._owner = owner
        self._vaccinated = vaccinated
        self._vaccinated_pets = self._pet_store_management["vaccinated_pets"]


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, pet_name):
        self._name = pet_name

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        self._species = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def vaccinated(self):
        return self._vaccinated

    def pet_got_vaccinated(self, pet):
        self._vaccinated = True
        self.mark_pet_vaccinated(pet)

    def mark_pet_vaccinated(self, pet):
        self._vaccinated_pets.append(pet)

    def check_if_vaccinated(self):
        return self._vaccinated

    def get_pet_human_years(self):
        return 7 * self.age

    def __eql__(self, other):
        if self._name == other.name and self._species == other.species:
            return True
        else:
            return False

    def pet_to_dict(self):
        return {
            "name": self._name,
            "species": self._species,
            "age": self._age,
            "owner": self._owner,
            "vaccinated": self._vaccinated

        }

    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}\nOwner: {self._owner}"


