cmake_minimum_required(VERSION 4.3)
project(SMBAClasses_C___)

set(CMAKE_CXX_STANDARD 23)

include_directories(.)

add_executable(SMBAClasses_C___
        main.cpp
        BADictsBackend.cpp
        BADictsBackend.h)

target_link_libraries(SMBAClasses_C___ PRIVATE stdc++exp)