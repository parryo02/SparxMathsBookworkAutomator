bookwork = []

print(
    '------------------------------\n'
    '|  Sparx Bookwork Automator  |\n'
    '|                            |\n'
    '|  What do you want to do?   |\n'
    '|                            |\n'
    '|  1: New task               |\n'
    '|  2: New question           |\n'
    '|  3: View answer            |\n'
    '|  4 or q: Quit              |\n'
    '------------------------------\n'
)

while True:
    userChoice = input('Enter your choice: ')
    if userChoice.lower == 'q':
        break
    