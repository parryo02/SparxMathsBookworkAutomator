//
// Created by Admin on 14/11/2026.
//

#include "BADictsBackend.h"


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

void BADictsBackend::increment_task() {
    taskCounter ++;
    questionCounter = '@';
    print(R"(
Task is: {}
Question is: {}
)", taskCounter, questionCounter);
}

void BADictsBackend::reset_tasks() {
    taskCounter = 1;
    print(R"(
Task is: {}, Question is: {}
)", taskCounter, questionCounter);
}

void BADictsBackend::new_answer() {
    questionCounter ++;

    print(R"(Enter answer for {}{}: )", taskCounter, questionCounter);

    getline(cin, bookwork[{taskCounter, questionCounter}]);
}

void BADictsBackend::view_answer() {
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

std::map<std::pair<std::size_t, char>, std::string> BADictsBackend::view_all() {
    return bookwork;
}

std::string BADictsBackend::view_all_formatted() {
    string output;
    for (const auto& [key, value] : bookwork) {
        std::size_t num = key.first;  // The size_t
        char letter = key.second;     // The char
        std::string text = value;     // The string

        output += std::format("({}, {}) -> {}\n", num, letter, text);
    }
    return output;
}