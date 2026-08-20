#!/usr/bin/env bash

read -r -p "Enter your age: " age

if [ "$age" -lt 0 ]; then
    echo "Invalid age. Please enter a valid age."
else
    echo "You are an adult."
fi
