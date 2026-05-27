bookwork = []
taskCounter = 1
questionCounter = 0

def increment_task():
    global taskCounter
    global questionCounter
    taskCounter += 1
    questionCounter = 0

    while len(bookwork) < taskCounter:
        bookwork.append([])

    print(
        "Task is: ", taskCounter, ", "
        "Question is: ", chr(questionCounter + 65).upper()
    )

def reset_tasks():
    global taskCounter
    taskCounter = 1
    print(
        "Task is: ", taskCounter
    )

def new_answer():
    global taskCounter
    global questionCounter
    questionCounter += 1

    while len(bookwork) < taskCounter:
        bookwork.append([])
    
    while len(bookwork[taskCounter - 1]) < questionCounter:
        bookwork[taskCounter - 1].append("")
    bookwork[taskCounter - 1][questionCounter - 1] = input(
        "Enter answer for " + str(taskCounter) + chr(questionCounter + 64).upper() + ": "
    )

def view_answer():
    task = ''
    question = ''
    while True:
        if task != '' and task.isdecimal() == True:
            break
        task = input("Task: ")
    while True:
        if question != '': #and question.isdecimal() == True:
            break
        question = ord(input("Question: ").lower()) - 96
    print(
        bookwork[int(task) - 1][int(question) - 1]
    )

def print_help():
    print(
        '|----------------------------|\n'
        '| 1 | New task               |\n'
        '| 2 | New question           |\n'
        '| 3 | View answer            |\n'
        '| 4 | Reset task counter     |\n'
        '| q | Quit                   |\n'
        '|----------------------------|\n'
    )

print(
    '|----------------------------|\n'
    '|  Sparx Bookwork Automator  |\n'
    '|                            |\n'
    '|  What do you want to do?   |\n'
    '|                            |\n'
    '|  1: New task               |\n'
    '|  2: New question           |\n'
    '|  3: View answer            |\n'
    '|  4: Reset task counter     |\n'
    '|  q: Quit                   |\n'
    '|----------------------------|\n'
)

while True:
    userChoice = input('Enter your choice: ')

    if userChoice.lower() == 'q':
        break

    match userChoice:
        case "1":
            increment_task()
        case "2":
            new_answer()
        case "3":
            view_answer()
        case "4":
            reset_tasks()
        case _:
            print_help()
print(bookwork)