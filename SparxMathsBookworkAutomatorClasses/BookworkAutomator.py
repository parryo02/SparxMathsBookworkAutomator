import BookworkAutomatorBackend as backend
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
            print(backend.increment_task())
        case "2":
            backend.new_answer()
        case "3":
            print(backend.view_answer())
        case "4":
            print(backend.reset_tasks())
        case _:
            print_help()
print(backend.bookwork)