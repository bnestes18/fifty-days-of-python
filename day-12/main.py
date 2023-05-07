# This function takes in a string that may or may not contain dots
# and returns the total number of dots within the string
def count_dots(dot_string):
    count = 0
    for char in dot_string:
        if char == '.':
            count += 1
    return count

print("count_dots function:", count_dots("he.lp."))


# Extra Challenge!!!
# This function prompts for a user's age and converts it into minutes.
def age_in_minutes():
    birth_year = input("Enter the 4-digit year that you were born: ")
    current_year = 2023
    minimum_birthyear = 1900
    days_per_year = 365
    hours_per_day = 24
    minutes_per_hr = 60
    if len(birth_year) < 4:
        raise ValueError('Invalid user input: The birth year must be 4 digits long.')
    elif int(birth_year) < minimum_birthyear or int(birth_year) > current_year:
        raise ValueError(f'Invalid user input: The birth year must be between %s and $s.', minimum_birthyear, current_year)
    age_years = (current_year - int(birth_year))
    age_minutes = (current_year - int(birth_year)) * days_per_year * hours_per_day * minutes_per_hr
    return "You are {} years old. Your age in minutes is: {:,}.".format(age_years, age_minutes)

print("age_in_minutes function:", age_in_minutes())
