import BookworkAutomatorDictsBackend as backend

task = ''
question = ''

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

def input_task():
    task = ''
    while True:
        if task != '' and task.isdecimal() == True and int(task) > 0:
            break
        task = input("Task: ")
    return task

def input_question():
    question = ''
    while True:
        if question != '':
            break
        question = input("Question: ").upper()
    return question

while True:
    userChoice = input('Enter your choice: ')

    if userChoice.lower() == 'q':
        break

    match userChoice:
        case "1":
            print(backend.increment_task())
        case "2":
            backend.new_answer(input(f'Enter answer for {backend.taskCounter}{chr(ord(backend.questionCounter) + 1)}: '))
        case "3":
            print(backend.view_answer(input_task(), input_question()))
        case "4":
            print(backend.reset_tasks())
        case _:
            print_help()

print(backend.bookwork)