cmake_minimum_required(VERSION 3.28)
project(PID C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(PID
        PID.c
        PID.h
        PID_Test.c)
