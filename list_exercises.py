def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_inputs = []
    for i in range(1, 6):
        user_input = int(input("Number:"))
        user_inputs.append(user_input)
    print("The first number is {}".format(user_inputs[0]))
    print("The last number is {}".format(user_inputs[4]))
    min_number = min(user_inputs)
    print("The smallest number is", min_number)
    max_number = max(user_inputs)
    print("The largest number is", max_number)
    average_number = sum(user_inputs) / len(user_inputs)
    print("The average of the numbers is", average_number)
    username = input("What is your name?:")
    usernames = set(usernames)
    if username in usernames:
        print("Access Grant")
    else:
        print("Access Denied")
main()