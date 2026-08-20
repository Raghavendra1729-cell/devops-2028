#!/usr/bin/env bash

read -r -p "Enter your age: " age

if ! [[ "$age" =~ ^[0-9]+$ ]]; then
    echo "Invalid age. Please enter a valid age."
elif [ "$age" -ge 18 ]; then
    echo "You are an adult."
else
    echo "You are a minor."
fi
