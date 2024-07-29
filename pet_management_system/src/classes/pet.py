from pet_management_system.config_provider import ConfigProvider
from pet_management_system.infra.logger import Logger


class Pet:
    def __init__(self, name, species, age, owner, vaccinated: bool):
        self._logger = Logger("pet_store_management.log").get_logger()
        config_path = ("E:\\5-tech\\Autmation\\Automation_Bootcamp\\QA_Automation\\pet_management_system"
                       "\\pet_store_management.json")
        self._pet_store_management = ConfigProvider().load_from_file(config_path)
        try:
            self.name = name
            self.species = species
            self.age = age
            self.owner = owner
            self._vaccinated = vaccinated
        except Exception as e:
            self._logger.error(f"Error in pet details: {e}")
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
        if self.name == other.name and self.species == other.species:
            return True
        else:
            return False

    def pet_to_dict(self):
        return {
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "owner": self.owner,
            "vaccinated": self._vaccinated

        }

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nOwner: {self.owner}"

pet = Pet("dhod","birds",2,"ehab",False)
pet.pet_got_vaccinated(pet)
