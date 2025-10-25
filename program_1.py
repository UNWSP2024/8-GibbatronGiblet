# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):

    personsInitials = ""
    usable_name = personsName.strip()
    middle_index = usable_name.find(' ') + 1
    last_index = usable_name.find(' ', middle_index) + 1
    first_initial = usable_name[0]
    middle_initial = usable_name[middle_index]
    last_initial = usable_name[last_index]
    personsInitials = f'{first_initial}. {middle_initial}. {last_initial}.'
    return personsInitials.strip()

personsName = input("Enter your first, middle, and last name:")

initials = initials_generator(personsName)

print(initials)

#This program was written by Logan Gibson on 10/23/25
#Its name is "Get Someone's Initials"