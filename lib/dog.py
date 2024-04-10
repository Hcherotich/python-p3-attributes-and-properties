class Dog:
    approved_breeds = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name="Mutt", breed="Mastiff"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
      if not isinstance(value, str) or not (1 <= len(value) <= 25):
        print("Name must be a string between 1 and 25 characters.")
        self._name = None  # Reset name attribute if invalid
      else:
         self._name = value
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in self.approved_breeds:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value
