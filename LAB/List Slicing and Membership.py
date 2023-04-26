# define your function here 
# make sure your function takes TWO parameters
def course_in_cse(courses, course_name):
    # fill in function body
    if course_name in courses:
        return course_name[3:] + ' is in the CSE course list.'
    return course_name[3:] + ' is not in the CSE course list.'

courses = ["CSE8A", "CSE8B", "CSE15L", "CSE100"]

# take in the user input here
user_input = input('What CSE course would you like to check for?: ')

# call and print your function output here
# sample function call: course_in_cse(courses, user_input)
print(course_in_cse(courses, user_input))