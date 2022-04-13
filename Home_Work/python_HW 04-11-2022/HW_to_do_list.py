to_do_list = []

while True:
    user_input = int(input("""Press 1 to add task
Press 2 to delete a task
Press 3 to view all tasks
Press 4 to quit
: """))

    if user_input == 4:
        break
    elif user_input == 1:
        to_do_task = input('What is the title of the task? ')
        to_do_priority = input('What is the priority of the task? ')
        next_chore = {'Task': to_do_task, 'Priority': to_do_priority}
        to_do_list.append(next_chore)
    elif user_input == 2:
        delete_chore = input('Ok which task would you like to delete? ')
        for chore in to_do_list:
            if delete_chore == chore['Task']:
                i = to_do_list.index(chore)
                del to_do_list[i]
    elif user_input == 3:
        for task in to_do_list:
            print("Task: " + task['Task'] + " " + "Priority: " + task['Priority'])
    else:
        print('Does not sound like any fun')


            # print(f"{task.index(task)} - {task['Task']} - {task['Priority']}")



