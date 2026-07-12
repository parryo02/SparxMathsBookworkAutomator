bookwork = {}
taskCounter = 1
questionCounter = '@'

def increment_task():
    global taskCounter
    global questionCounter
    taskCounter += 1
    questionCounter = '@'

    """
    while len(bookwork) < taskCounter:
        bookwork.append([])
    """

    print(
    f"""Task is: {taskCounter}
    Question is: {questionCounter}"""
    )

def reset_tasks():
    global taskCounter
    global questionCounter
    taskCounter = 1
    questionCounter = '@'
    print(
    f"""Task is: {taskCounter}
    Question is: A"""
    )

def new_answer():
    global taskCounter
    global questionCounter
    questionCounter = chr(ord(questionCounter) + 1)

    """
    while len(bookwork) < taskCounter:
        bookwork.append([])
    while len(bookwork[taskCounter - 1]) < questionCounter:
        bookwork[taskCounter - 1].append("")
    """

    bookwork.update({(taskCounter, questionCounter) : input(f'Enter answer for {taskCounter}{questionCounter}: ')})

def view_answer():
    task = ''
    question = ''
    while True:
        if task != '' and task.isdecimal() == True and int(task) > 0:
            break
        task = input("Task: ")
    while True:
        if question != '':
            break
        question = input("Question: ").upper()
    try:
        print(bookwork[(int(task), question)])
    except KeyError:
        print("Answer not found for that task/question combination")
def print_help():
    print(
    """
|----------------------------|
| 1 | New task               |
| 2 | New question           |
| 3 | View answer            |
| 4 | Reset task counter     |
| q | Quit                   |
|----------------------------|
    """
    )

print(
"""
|----------------------------|
|  Sparx Bookwork Automator  |
|                            |
|  What do you want to do?   |
|                            |
|  1: New task               |
|  2: New question           |
|  3: View answer            |
|  4: Reset task counter     |
|  q: Quit                   |
|----------------------------|
"""
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