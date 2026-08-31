#!/usr/bin/env bash

read -r -p "Enter your name: " name
read -r -p "Enter your roll number: " roll_number
read -r -p "Enter your comment: " comment

current_date=$(date)
host_name=$(hostname)
user_name=$(whoami)
report_directory="system_report"
process_file="$report_directory/processes.txt"

mkdir -p "$report_directory"
touch "$process_file"

echo ""
echo "=== System Information ==="
echo "Current date: $current_date"
echo "Hostname: $host_name"
echo "Username: $user_name"

echo ""
echo "=== Disk Usage ==="
df -h

echo ""
echo "=== Running Processes ==="
ps aux > "$process_file"
echo "Process information saved to $process_file"
cat "$process_file"

echo ""
echo "=== Student Details ==="
echo "My name is $name"
echo "My roll number is $roll_number"
echo "My comment is: $comment"
