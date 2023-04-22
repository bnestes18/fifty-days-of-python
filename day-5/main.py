# This function returns the total price (based on user input) after a discount is applied
def my_discount():
    price = input("Enter the price of the item: ")
    percentage = input("Enter the discount percentage of the item: ")
    discount = int(percentage.strip("%"))/100
    final_price = int(price) - (int(price) * discount)
    text = "The total is {:.2f} dollars"
    return text.format(final_price)

print("my_discount function:", my_discount())

# Extra Challenge!!!
# This function takes in a list of students by gender (male/female), and returns the count
# of each as a list of tuples
def total_students(students):
    count_male, count_female = 0, 0
    for s in students:
        if s.lower() == "female":
            count_female += 1
        else:
            count_male += 1
    tuple_male = ('Male', count_male)
    tuple_female = ('Female', count_female)
    return [tuple_male, tuple_female]

print("total_students function:", total_students(['Male','Female','female','male','male','male','female','male','Female','Male','Female','Male','female']))