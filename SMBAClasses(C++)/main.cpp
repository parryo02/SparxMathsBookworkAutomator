#include <iostream>
#include <vector>
#include <string>
#include <format>
#include <print>
#include <stdexcept>
#include <map>
#include <utility>
#include <cctype>

#include "BADictsBackend.h"

using namespace std;

string userChoice {};

void print_help() {
    cout << R"(
|----------------------------|
| 1 | New task               |
| 2 | New question           |
| 3 | View answer            |
| 4 | Reset task counter     |
| q | Quit                   |
|----------------------------|
)" << '\n';
}

int main() {
    BADictsBackend backend;
    print(R"(
|----------------------------|
|  Sparx Bookwork Automator  |
|                            |
|  What do you want to do?   |)");
        print_help();

        while (true) {
            print("Enter your choice: "); getline(cin, userChoice);

            if  ((userChoice[0] | 0x20) == 'q') {break;};

            switch (userChoice[0]) {
                case '1':
                    cout << backend.increment_task();
                    break;
                case '2':
                    backend.new_answer();
                    break;
                case '3':
                    backend.view_answer();
                    break;
                case '4':
                    cout << backend.reset_tasks();
                    break;
                default:
                    print_help();
                    break;
            };
        }

        print("{}", backend.view_all_formatted());

}