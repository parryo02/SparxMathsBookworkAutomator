//
// Created by Admin on 14/11/2026.
//

#ifndef SMBACLASSES_C____BADICTSBACKEND_H
#define SMBACLASSES_C____BADICTSBACKEND_H

#include <map>
#include <string>
#include <utility>
#include <cstddef>   // for std::size_t (or <cstdlib> / <cstring> etc.)


class BADictsBackend {
public:
    std::string increment_task();
    std::string reset_tasks();
    void new_answer();
    void view_answer();
    std::map<std::pair<std::size_t, char>, std::string> view_all();
    std::string view_all_formatted();
private:
    std::map<std::pair<std::size_t, char>, std::string> bookwork;
    std::size_t taskCounter {1};
    char questionCounter {'@'};

};


#endif //SMBACLASSES_C____BADICTSBACKEND_H
