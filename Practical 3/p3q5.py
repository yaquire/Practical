
while True:
    user_input = input("Your Input (\"E\" to exit) : ")

    if user_input.lower() == 'hello':
        print('This will be printed only when user input "hello"')
        pass  # Do nothing for 'hello'

    elif user_input.lower() == 'e':
        print("Exit the while loop.")
        break  # Exit the while loop for 'e'

    else:
        print(f'Other Input: {user_input}')
