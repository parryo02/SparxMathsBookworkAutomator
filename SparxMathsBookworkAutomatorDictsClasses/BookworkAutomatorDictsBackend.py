bookwork = {}
taskCounter = 1
questionCounter = 'A'

def increment_task():
    global taskCounter
    global questionCounter
    taskCounter += 1
    questionCounter = 'A'

    return f"""Task is: {taskCounter}
Question is: {questionCounter}"""

def reset_tasks():
    global taskCounter
    global questionCounter
    taskCounter = 1
    questionCounter = 'A'
    return f"""Task is: {taskCounter}
Question is: {questionCounter}"""

def new_answer(answer):
    global taskCounter
    global questionCounter
    
    bookwork.update({(taskCounter, questionCounter) : answer})
    try:
        return (
            f'Task is: {taskCounter}\n'
            f'Question is: {chr(ord(questionCounter) + 1)}'
            )
    finally:
        questionCounter = chr(ord(questionCounter) + 1)

def view_answer(task, question):
    try:
        return bookwork[(int(task), question)]
    except KeyError:
        return "Answer not found for that task/question combination"