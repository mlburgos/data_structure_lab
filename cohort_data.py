def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called "houses" that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army"
            ])

    """

    # Code goes here
    houses_file = open(filename)

    houses = set(line.rstrip().split("|")[2] for line in houses_file if line.rstrip().split("|")[2] != "")
    return houses


def get_full_name(line):
    """Return first and last name as a string."""

    name_list = line.rstrip().split("|")[0:2]    

    return name_list[0] + " " + name_list[1]

def get_last_name(line):
    """Return first and last name as a string."""

    return line.rstrip().split("|")[1] 



def get_house(line):
    """Return house."""
    
    return line.rstrip().split("|")[2]



def get_cohort(line):
    """Return cohort."""

    cohort = line.rstrip().split("|")[-1]

    return cohort

# print get_cohort("Harry|Potter|Gryffindor|McGonagall|Fall 2015")

def sort_by_cohort(filename):
    """TODO: Sort students by cohort, skipping instructors.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name. Puts ghosts into a separate list entitled "ghosts".
    Returns a list of these lists.

        ex. fall_15 = ["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ""Hermione Granger", ... ]
        ex. all_students = [["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ...],
        ["Lee Jordan", "Andrew Kirke", "Neville Longbottom", ...],
        ["Cormac McLaggen", "Parvati Patil", "Jimmy Peakes", ...],
        ["Euan Abercrombie", "Katie Bell", "Lavender Brown", ...]]

    """

    lines = [line.rstrip() for line in open(filename)]

       # info = open(filename)  # for some reason, this object "disapears" once it's been looped over
    # using "info = open(filename)" and then using "info" instead of "lines" in the
    # for loops of the various list comprehensions doesn't work because...
    # I have no idea

    fall_15 = sorted([get_full_name(line) for line in lines if get_cohort(line) == "Fall 2015"])

    winter_16 = sorted([get_full_name(line) for line in lines if get_cohort(line) == "Winter 2016"])

    spring_16 = sorted([get_full_name(line) for line in lines if get_cohort(line) == "Spring 2016"])

    summer_16 = sorted([get_full_name(line) for line in lines if get_cohort(line) == "Summer 2016"])

    ghosts = sorted([get_full_name(line) for line in lines if get_cohort(line) == "G"])

    all_students = [fall_15,
                    winter_16,
                    spring_16,
                    summer_16,
                    ghosts,
                    ]

    return all_students



def students_by_house(filename):
    """TODO: Sort students by house.


    Iterates over the data to create a list for each house, and sorts students
    into their appropriate houses by last name. Sorts ghosts into a list called "ghosts"
    and instructors into a list called "instructors".
    Returns all lists in one list of lists.

        ex. gryffindor = ["Abercrombie", "Bell", "..." ]
        ex. ghosts = ["Baron", "Friar", "..."]
        ex. all_students = [ hufflepuff,
                    gryffindor,
                    ravenclaw,
                    slytherin,
                    dumbledores_army,
                    ghosts,
                    instructors
        ]

    """

    lines = [line.rstrip() for line in open(filename)]



    gryffindor = [] 
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    ravenclaw = []
    ghosts = []
    instructors = []

    all_students = {'hufflepuff': [],
                    'gryffindor': [],
                    'ravenclaw': [],
                    'slytherin': [],
                    'dumbledores_army': [],
                    'ghosts': [],
                    'instructors': [],
                    }

    for cohort in all_students:
        if cohort == 'ghosts' or cohort == 'instructors':
            all_students[cohort] = sorted([get_last_name(line) for line in lines if get_cohort(line).lower() == cohort])
    # Code goes here

    return all_students


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. student_list = [
                ("Euan Abercrombie", "Gryffindor", "McGonagall", "Summer 2016"),
                ("Katie Bell", "Gryffindor", "McGonagall", "Summer 2016"),
                # ...
            ]
    """

    student_list = []

    # Code goes here

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Uses the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name from the command line, returns that
    student's cohort, or returns "Student not found." when appropriate. """

    # Code goes here

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student last names that have duplicates.

    Iterates over the data to find any last names that exist across all cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Weasley"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and when given a name, print a statement of everyone in their house in their cohort.

    Uses the list of tuples generated by all_students_tuple_list to make a small function
    that, when given a student's first and last name, print students that are in both
    that student's cohort and that student"s house.

    ex: Choose a student: Hermione Granger
        Hermione Granger was in house Gryffindor in the Fall 2015
        cohort.
        The following students are also in their house:
        Seamus Finnigan
        Angelina Johnson
        Harry Potter
        Ron Weasley
        Oliver Wood


    """

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!

# print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
print students_by_house("cohort_data.txt")
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
