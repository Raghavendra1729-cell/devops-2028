# Shell Scripting

This folder contains my Session 3 Bash practice. Each script focuses on one small concept, and `system_info.sh` combines the commands required for the homework.

## Homework checklist

| Requirement | Used in `system_info.sh` |
| --- | --- |
| Current date, hostname, and username | `date`, `hostname`, `whoami` |
| Disk usage and running processes | `df -h`, `ps aux` |
| Variables and user input | Shell variables and `read -r -p` |
| Create a directory and file | `mkdir -p`, `touch` |
| Save process output | `ps aux > system_report/processes.txt` |
| Print clear output | `echo` and `cat` |

## Run all scripts

```bash
chmod +x *.sh
./hello.sh
./data.sh
./script1.sh
./input.sh
./variable.sh
./function.sh
./loop.sh
./system_info.sh
./condition.sh
./while_loop.sh
./while_loop1.sh
```

## 1. Create a folder and file — `hello.sh`

`mkdir -p` creates a folder. `>` writes text into a file and `cat` prints the file content.

```bash
#!/usr/bin/env bash

mkdir -p hello
printf '%s\n' "This is my logfile" > hello/app.log
cat hello/app.log
```

**Terminal output**

```text
This is my logfile
```

## 2. Overwrite a file — `data.sh`

The `>` operator overwrites an existing file. The second write replaces the first line.

```bash
#!/usr/bin/env bash

mkdir -p data
printf '%s\n' "This is a log file." > data/app.log
cat data/app.log
printf '%s\n' "This is my file" > data/app.log
cat data/app.log
```

**Terminal output**

```text
This is a log file.
This is my file
```

## 3. Append to a file — `script1.sh`

The `>>` operator appends content to a file and keeps the previous content.

```bash
#!/usr/bin/env bash

mkdir -p test
echo "This is file1" > test/app.log
echo "This is file2" >> test/app.log
cat test/app.log
```

**Terminal output**

```text
This is file1
This is file2
```

## 4. Take input — `input.sh`

`read` takes input from the user and stores it in a variable. `$name` prints the value stored in `name`.

```bash
#!/usr/bin/env bash

read -r -p "Enter your name: " name
read -r -p "Enter your roll number: " roll_number
read -r -p "Enter your comment: " comment

echo "My name is $name"
echo "My roll number is $roll_number"
echo "My comment is: $comment"
```

**Input used:** `Raghavendra`, `24BCS10250`, `Learning Bash`

**Terminal output**

```text
My name is Raghavendra
My roll number is 24BCS10250
My comment is: Learning Bash
```

## 5. Variables — `variable.sh`

Variables store data for reuse. Variables are assigned without spaces and read with `$variable_name`.

```bash
#!/usr/bin/env bash

name="Raghavendra"
roll_number="24BCS10250"
comment="learning Bash"

echo "My name is $name"
echo "My roll number is $roll_number"
echo "I am $comment"
```

**Terminal output**

```text
My name is Raghavendra
My roll number is 24BCS10250
I am learning Bash
```

## 6. Function — `function.sh`

A function groups commands under one name. The function runs when its name is called.

```bash
#!/usr/bin/env bash

show_info() {
    echo "This is a function"
    echo "This is a function to show information"
}

show_info
```

**Terminal output**

```text
This is a function
This is a function to show information
```

## 7. For loop — `loop.sh`

A `for` loop repeats commands while its condition is true. This loop starts at 0, runs through 5, and increases `i` after every iteration.

```bash
#!/usr/bin/env bash

for ((i=0;i<=5;i++)); do
    echo "This is iteration number $i"
done
```

**Terminal output**

```text
This is iteration number 0
This is iteration number 1
This is iteration number 2
This is iteration number 3
This is iteration number 4
This is iteration number 5
```

## 8. Complete system report — `system_info.sh`

This is the main homework script. It takes student details as input, stores command results in variables, creates a report directory and file, prints disk usage and running processes, and saves the process list using output redirection.

```bash
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
```

**Sample input:** `Raghavendra`, `24BCS10250`, `Learning Bash`

**Sample Ubuntu terminal output**

```console
ubuntu@ip-172-31-24-18:~/devops-2028/shellscripting$ ./system_info.sh
Enter your name: Raghavendra
Enter your roll number: 24BCS10250
Enter your comment: Learning Bash

=== System Information ===
Current date: Mon Aug 31 12:45:20 UTC 2026
Hostname: ip-172-31-24-18
Username: ubuntu

=== Disk Usage ===
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       7.6G  2.4G  5.2G  32% /
tmpfs           475M     0  475M   0% /dev/shm

=== Running Processes ===
Process information saved to system_report/processes.txt
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.5  21932 12840 ?        Ss   10:29   0:02 /sbin/init
ubuntu    2481  0.0  0.2  17820  6120 pts/0    Ss   12:42   0:00 -bash
... remaining processes omitted here for readability ...

=== Student Details ===
My name is Raghavendra
My roll number is 24BCS10250
My comment is: Learning Bash
```

The terminal block is a short sample from an Ubuntu-style environment. The script itself prints and saves the complete process list; dates, hostnames, disk values, and process IDs change on every run.

## 9. If-else condition — `condition.sh`

An `if` statement checks a condition. `else` runs when the condition is false. This version has no `elif` branch.

```bash
#!/usr/bin/env bash

read -r -p "Enter your age: " age

if [ "$age" -lt 0 ]; then
    echo "Invalid age. Please enter a valid age."
else
    echo "You are an adult."
fi
```

**Input used:** `21`

**Terminal output**

```text
You are an adult.
```

## 10. While loop with input — `while_loop.sh`

A `while true` loop repeats until `break` stops it. This script accepts numbers until the user enters `q`.

```bash
#!/usr/bin/env bash

while true; do
    read -r -p "Enter a number (or 'q' to quit): " input

    if [[ "$input" == "q" ]]; then
        echo "Exiting the loop."
        break
    elif ! [[ "$input" =~ ^[0-9]+$ ]]; then
        echo "Invalid input. Please enter a valid number."
        continue
    fi

    echo "You entered: $input"
done
```

**Input used:** `7`, then `q`

**Terminal output**

```text
You entered: 7
Exiting the loop.
```

## 11. While loop counter — `while_loop1.sh`

A `while` loop runs while its condition is true. `count` increases after each iteration until it reaches 5.

```bash
#!/usr/bin/env bash

count=0

while [ "$count" -lt 5 ]; do
    echo "This is iteration number $count"
    ((count++))
done
```

**Terminal output**

```text
This is iteration number 0
This is iteration number 1
This is iteration number 2
This is iteration number 3
This is iteration number 4
```
