import json
from pet_management_system.file_handler import FileHandler
from pet_management_system.src.classes.utils import Utils


class Owner:
    def __init__(self, owners_name, phone_number, pets: list):
        self._file_path = Utils().setup_environment(__file__, "../../pet_store_management.json", "../../")
        self._pet_store_management = FileHandler(self._file_path, 'r+')
        self._owners_name = owners_name
        self._phone_number = phone_number
        self._pets = pets
        self._total_pets = self.get_all_pets()

    @property
    def owners_name(self):
        return self._owners_name

    @owners_name.setter
    def owners_name(self, value):
        self._owners_name = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def pets(self):
        return self._pets

    @pets.setter
    def pets(self, value):
        self._pets = value

    def add_pet_to_list(self, pet):
        if pet.check_if_vaccinated():
            self.pets.append(pet)
        else:
            return f"{pet.name} is not vaccinated"

    def remove_pet_from_list(self, pet):
        self.pets.remove(pet)

    def add_owner(self):
        self._pet_store_management["owners"].append(self.owner_to_dict())
        with open(self._file_path, 'w') as f:
            f.write(json.dumps(self._pet_store_management, indent=2))

    def get_all_pets(self):
        all_pets = []
        for owner in self._pet_store_management["owners"]:
            all_pets.extend(owner.get("pets", []))
        return all_pets

    def total_pets_count(self):
        return len(self.get_all_pets())

    def owner_to_dict(self):
        return {
            "owners_name": self._owners_name,
            "phone_number": self._phone_number,
            "pets": self._pets
        }

    def __str__(self):
        return f"The owner {self._owners_name} have the following pets: {self._pets}"
