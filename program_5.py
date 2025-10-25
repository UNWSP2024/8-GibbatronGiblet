# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.


def main():
    relevant_courses, subject = subject_search(catalog_creation())
    print(f'''The relevant courses are {relevant_courses}.''')
    print(f'The subject is {subject}.')

def catalog_creation():
    catalog = {}
    count = 1
    course_num = int(input("How many courses would you like to enter?"))
    for i in range(course_num):
        course_ID = input(f"Enter course {count}'s ID: ")
        course_name = input(f"Enter course {count}'s name: ")
        catalog[course_name] = course_ID
        count += 1
    return catalog

def subject_search(catalog):
    subject = input("Enter subject name: ")
    relevant_courses = []
    for course in catalog:
        if subject in catalog[course]:
            relevant_courses.append(course)
    return relevant_courses, subject
if __name__ == "__main__":
    main()
#This program was written by Logan Gibson on 10/23/25
#Its name is "Mini Course Catalog"