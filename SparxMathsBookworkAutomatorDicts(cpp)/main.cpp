#include <iostream>
#include <vector>
#include <string>
#include <format>
#include <print>
#include <stdexcept>
#include <map>
#include <utility>
#include <cctype>

using namespace std;

map<pair<size_t, char>, string> bookwork;
size_t taskCounter {1};
char questionCounter {'@'};
string userChoice {};

void increment_task() {
    taskCounter ++;
    questionCounter = '@';
    print(R"(
Task is: {}
Question is: {}
)", taskCounter, questionCounter);
}

void reset_tasks() {
    taskCounter = 1;
    print(R"(
Task is: {}, Question is: {}
)", taskCounter, questionCounter);
}

void new_answer() {
    questionCounter ++;

    print(R"(Enter answer for {}{}: )", taskCounter, questionCounter);

    getline(cin, bookwork[{taskCounter, questionCounter}]);
}

void view_answer() {
    size_t task{0};
    string question{};
    string taskInput;

    while (true) {
        print("Task: ");
        getline(cin, taskInput);

        try {
            task = stoull(taskInput);
            if (task > 0) break;
        } catch (...) {
            continue;
        }
    }

    while (true) {
        print("Question: ");
        getline(cin, question);

        question = toupper(question[0]);

        if (question != "") {
            break;
        }
    }

    try {
        string answer = bookwork.at({task, question[0]});
        println("{}", answer);
    }
    catch (const out_of_range& e) {
        println("Answer not found for that task/question combination");
    }
}

void print_help() {
    print(R"(
|----------------------------|
| 1 | New task               |
| 2 | New question           |
| 3 | View answer            |
| 4 | Reset task counter     |
| q | Quit                   |
|----------------------------|
)");
}

int main() {
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
                    increment_task();
                    break;
                case '2':
                    new_answer();
                    break;
                case '3':
                    view_answer();
                    break;
                case '4':
                    reset_tasks();
                    break;
                default:
                    print_help();
                    break;
            };
        }

        print("{}", bookwork);
}