# to change people edit this list
clients = ['harry', 'rohan', 'hammad', 'hussain']
# currently only these two operations are supported
operations = ['create a log', 'retrieve from a log']
types = ['food', 'exercise']
messages = ['What operation do you want to perform?:',
            'For which client do you want to add info?',
            'Food or Exercise?']
choice_of_usr = 0


def main_function():
    print("\t\t\t\t-------------------------------------")
    print("\t\t\t\t Welcome to Health Management System")
    print("\t\t\t\t-------------------------------------")
    operations_ans = operation_manager(0, operations)
    clients_ans = operation_manager(1, clients)
    types_ans = operation_manager(2, types)
    if operations_ans == 0:
        with open(f"{clients[clients_ans]}-{types[types_ans]}.txt", "a") as logfile:
            log = str(input(f"What did {clients[clients_ans].capitalize()} eat? " if types_ans ==
                      0 else f"What exercise did {clients[clients_ans].capitalize()} do? "))
            if log == '':
                print("The Program will exit now... because you didn't write anything")
                print("Program Exited successfully")
                quit()
            timestamp = getDateTime()
            log = f"[ {timestamp} ] " + log
            logfile.write(log)
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
            print(f"There are no logs for {clients[clients_ans].capitalize()}")
    return "Operation Successful"


def operation_manager(choice_maker, operand):
    """Takes two parameters.

    choice_maker is list containing data as parameter.

    choice_maker takes 1 or 0. 0 means operation 1 means clients 2 means type (either food or exercise) in case of operation_function
    """
    print_options(choice_maker, operand)
    ans = choice(choice_maker, operand)
    return ans


def choice(type_of_inp, operand):
    """:param type_of_inp:0 or 1 | 0 for operation, 1 for client, 2 for 
         operand: a list which contains the content 

        This function takes the choice of user based on the parameters passed
    """
    global choice_of_usr  # initialized at the end of the file
    types_of_inp = ["operation", "client", "type"]
    if str(choice_of_usr) == 'q' or str(choice_of_usr) == '':
        print("The Program will exit now...")
    main_choice = types_of_inp[type_of_inp]
    choice_of_usr = str(input(
        "\nPlease choose one of the options above: (type the "+main_choice+" name or "+main_choice+" number): "))

    def check_choice(choice_maker, operand):
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
                return -1
            found = False
            if found == False:
                for i in range(0, len(operand)):
                    if choice_of_usr.lower() == operand[i]:
                        found = True
                        return i
            else:
                print("You entered an incorrect name. try again!")
                print_options(operand)
                return choice(choice_maker, operand)
    ans = check_choice(type_of_inp, operand)
    check_status(ans)
    return ans


def print_options(choice_maker, operand):
    print('\n')
    print(f"{messages[choice_maker]}")
    print('\n')
    for x in range(len(operand)):
        print(f"\t{x+1}. {operand[x].capitalize()}")


def check_status(status):
    if status == -1:
        print("Program Exited successfully")
        quit()


def getDateTime():
    import datetime
    return datetime.datetime.now()


print(main_function())
