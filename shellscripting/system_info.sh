#!/usr/bin/env bash

read -r -p "Enter your name: " name
read -r -p "Enter your roll number: " roll_number
read -r -p "Enter your comment: " comment

current_date=$(date)
host_name=$(hostname)
user_name=$(whoami)

echo "Current date: $current_date"
echo "Hostname: $host_name"
echo "Username: $user_name"
ps -p "$$" -o pid,tty,time,comm > process.log
echo "Process information saved to process.log"
cat process.log
echo "My name is $name"
echo "My roll number is $roll_number"
echo "My comment is: $comment"
