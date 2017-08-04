# -----------------
# PART TWO: QUERIES
# -----------------

# Get the human with the id 2.
q1 = Human.query.get(2)

# Get all of the animals for the human with the id 5 and the animal species 'dog'
q2 = Animal.query.filter_by(animal_species='dog', human_id=5).all()

# Get all the animals that were born after 2015 (do not include animals without birth years).
q3 = Animal.query.filter(Animal.birth_year > 2015).all()

# Find the customers with first names that start with 'J'
q4 = Human.query.filter(Human.fname.startswith('J')).all()

# Find all the animals without birth years in the database.
q5 = Animal.query.filter_by(birth_year=None).all()

# Find all animals that are either fish or rabbits
q6 = Animal.query.filter((Animal.animal_species=="fish") | (Animal.animal_species=="rabbit")).all()

# Find all the humans whose email addresses do not contain 'gmail'
from SQLAlchemy import not_
q7 = Human.query.filter(not_(Human.email.like('%gmail%'))).all()

# ---------------------
# PART THREE: FUNCTIONS
# ---------------------

# 1. Write a function, print_customer_directory, which does not take any arguments
#    and prints out each customer (once) with a list of their pets.

#    The output should look like this (with tabs to indent each animal name under
#    a human's name)

#       Human_first_name Human_last_name
#           Animal name (animal species)
#           Animal name (animal species)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)

def print_customer_directory():
    """"""
    pass

# 2. Write a function, get_animals_by_name, which takes in a string representing an animal name
#    (or part of an animal name) and *returns a list of animals* whose names
#    contain that string.

def get_animals_by_name(name):
    """"""
    pass

# 3. Write a function, find_humans_by_animal_species, which takes in an animal
#    species and *returns a list* of all of the humans who have animals of that species.

def find_humans_by_animal_species(species):
    """"""
    pass
