import emoji

def your_vat():
    user_price = ""
    user_vat = ""
    try:
        while not user_price or not user_vat:
            user_price = input("Enter the price: ")
            user_vat = input("Enter the Value-Added Tax (VAT). Must include '%' sign!: ")
            user_vat = user_vat.strip('%')
            vat_price = int(user_price) + int(user_price) * int(user_vat) / 100 
            return "Your VAT is ${:.2f}".format(vat_price)
    except ValueError:
        print("Cannot compute the VAT. Please ensure that only numbers are provided!")

print("your_vat function:", your_vat())


def python_snakes(num):
    snake = emoji.emojize(":snake:")
    snake_pair = snake * 2 + " "
    snake_string = ""
    i = 1
    for i in range(i, num, 1):
        snake_string += snake_pair * i + '\n'
    print(snake_string)   

print("python_snakes function", python_snakes(7))