from pet_class import Pet

#user's input(name,type,age of the pet)

pet_name = input(" What's the name of your pet? ")
pet_animal_type = input(" What's your pet's animal type? ")
pet_age = input (" What's the age of your pet? ") 

#object of the pet
pet_object = Pet(pet_name, pet_animal_type, pet_age)
 
#display
print(pet_object.get_name())
print(pet_object.get_animal_type())
print(pet_object.get_age())