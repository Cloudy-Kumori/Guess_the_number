import random

number = random.randint(1, 100)
user_input = input('''Hi, I'm Cloudy. Let's play a guess number game! 
Please input a integer number between 1 and 100, and I'll tell you if it's bigger or smaller. :''')
def check_ifnumber(user_input):
    while not user_input.isdigit():
        user_input = input('Invalid input, please try again! :')
        continue
    else:
        user_input = int(user_input)
        return user_input

user_input=check_ifnumber(user_input)
while user_input != number:
    if user_input in range(1, 101):
        if user_input > number:
            user_input = input('The number you input is big, try again! :')
            user_input = check_ifnumber(user_input)
        elif user_input < number:
            user_input = input('The number you input is small, try again! :')
            user_input = check_ifnumber(user_input)
        elif user_input == number:
            print('Congratulations! You are right, the number is', number)
            input('Press any key to exit.')
            break
    else:
        user_input=input('Oops! The number you entered is not between 1-100, try again! :')
        user_input = check_ifnumber(user_input)
else:
    print('Congratulations! You are right, the number is', number, '!')
    input('Press any key to exit.')
