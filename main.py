import os
# change the directory to main.py
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)
if not os.path.exists("clients"):
    os.mkdir("clients")
# to change people edit this list
clients = ['harry', 'rohan', 'hammad', 'hussain']
# currently only these two operations are supported
operations = ['create a log', 'retrieve from a log']
# types of log - can be changed and more can be added
types = ['food', 'exercise']
messages = ['What operation do you want to perform?:',
            'For which client do you want to add info?',
            'Food or Exercise?']  # messages printed before the list of options
choice_of_usr = 0


def main_function():
    print("\t\t\t\t-------------------------------------")
    print("\t\t\t\t Welcome to Health Management System")
    print("\t\t\t\t-------------------------------------")
    operations_ans = choice(0, operations)
    clients_ans = choice(1, clients)
    types_ans = choice(2, types)
    if operations_ans == 0:
        with open(f"./clients/{clients[clients_ans]}-{types[types_ans]}.txt", "a") as logfile:
            log = str(input(f"What did {clients[clients_ans].capitalize()} eat? " if types_ans ==
                      0 else f"What exercise did {clients[clients_ans].capitalize()} do? "))
            if log == '':
                print("The Program will exit now... because you didn't write anything")
                print("Program Exited successfully")
                quit()
            timestamp = getDateTime()
            log = f"[ {timestamp} ] " + log
            logfile.write(log + "\n")
            # print(log)
    else:
        try:
            with open(f"{clients[clients_ans]}-{types[types_ans]}.txt", "r") as logfile:
                print(
                    f"\n\t\tDisplaying {types[types_ans].capitalize()} Logs for {clients[clients_ans].capitalize()}")
                print("----------------------------------------------------------------")
                for line in logfile:
                    print("\n\t", line)
                print("\n\t\t\tEND OF FILE\n")
                print("----------------------------------------------------------------")
        except:
            print(
                f"There are no logs in {types[types_ans]} for {clients[clients_ans].capitalize()}")
    return "Operation Successful"


def choice(type_of_inp, operand):
    """:param type_of_inp:0 or 1 | 0 for operation, 1 for client, 2 for 
         operand: a list which contains the content 

        This function takes the choice of user based on the parameters passed
    """
    global choice_of_usr  # initialized at the end of the file
    types_of_inp = ["operation", "client", "type"]
    main_choice = types_of_inp[type_of_inp]
    print_options(type_of_inp, operand)
    choice_of_usr = str(input(
        "\nPlease choose one of the options above: (type the "+main_choice+" name or "+main_choice+" number): "))

    def validate_choice(choice_maker, operand):
        try:
            if int(choice_of_usr) <= len(operand):
                return int(choice_of_usr) - 1
            else:
                print("You entered an incorrect number. try again!")
                print_options(operand)
                return choice(choice_maker, operand)
        except Exception as e:
            if choice_of_usr == 'q' or choice_of_usr == '':
                print("The Program will exit now...")
                print("Program Exited successfully")
                quit()

            found = False
            for i in range(0, len(operand)):
                if choice_of_usr.lower() == operand[i]:
                    found = True
                    return i
            if not found:
                print("You entered an incorrect name. try again!")
                return choice(choice_maker, operand)

    ans = validate_choice(type_of_inp, operand)
    return ans


def print_options(choice_maker, operand):
    print('\n')
    print(f"{messages[choice_maker]}")
    print('\n')
    for x in range(len(operand)):
        print(f"\t{x+1}. {operand[x].capitalize()}")


def getDateTime():
    import datetime
    return datetime.datetime.now()


print(main_function())
