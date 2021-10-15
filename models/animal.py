class Animal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, breed, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id

animal1 = Animal(1, 'Jack', 'husky', 'napping', 1, 2)
print(animal1.name)
