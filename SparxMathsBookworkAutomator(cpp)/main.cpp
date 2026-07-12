#include <iostream>
#include <vector>
#include <string>
#include <format>
#include <print>
#include <stdexcept>

using namespace std;

vector<vector<string>> bookwork;
size_t taskCounter {1};
size_t questionCounter {0};
string userChoice {};

void increment_task() {
    taskCounter ++;
    questionCounter = 0;
    bookwork.emplace_back();
    cout << format(R"(
Task is: {}
Question is: {}
)", taskCounter, questionCounter);
}

void reset_tasks() {
    taskCounter = 1;
    cout << format(R"(
Task is: {}
)", taskCounter);
}

void new_answer() {
    questionCounter ++;

    if (bookwork.size() < taskCounter) {
        bookwork.resize(taskCounter);
    }

    if (bookwork.at(taskCounter - 1).size() < questionCounter) {
        bookwork.at(taskCounter - 1).resize(questionCounter);
    }

    cout << format(R"(Enter answer for {}{}: )"
    , taskCounter, static_cast<char>(questionCounter + 64));

    getline(cin, bookwork.at(taskCounter - 1).at(questionCounter - 1));
}

void view_answer() {
    size_t task{0};
    size_t question{0};
    string taskInput;
    string questionInput;

    // 1. Task Input Loop (Validates it's an integer > 0)
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

    // 2. Question Input Loop (Validates it's an alphabet letter mapping > 0)
    while (true) {
        print("Question: ");
        getline(cin, questionInput);

        if (!questionInput.empty()) {
            char letter = questionInput[0];
            int calculatedIndex = (letter | 0x20) - 96;

            if (calculatedIndex > 0) {
                question = static_cast<size_t>(calculatedIndex);
                break;
            }
        }
    }

    try {
        string answer = bookwork.at(task - 1).at(question - 1);
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