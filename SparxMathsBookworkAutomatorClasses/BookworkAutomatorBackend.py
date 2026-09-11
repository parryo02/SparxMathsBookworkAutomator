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

    return f'Task is: {taskCounter}\nQuestion is: {chr(questionCounter + 65).upper()}'

def reset_tasks():
    global taskCounter
    taskCounter = 1
    return f'Task is: {taskCounter}'

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
        if task != '' and task.isdecimal() == True and int(task) > 0:
            break
        task = input("Task: ")
    while True:
        if question != '' and int(question) > 0:
            break
        question = ord(input("Question: ").lower()) - 96
    try:
        return bookwork[int(task) - 1][int(question) - 1]
    except IndexError:
        return "Answer not found for that task/question combination"