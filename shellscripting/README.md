# Session 3 Bash Tasks

Each section has the theory, the code written for the task, and output from a successful terminal run.

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

## 8. System information and process file — `system_info.sh`

`date`, `hostname`, and `whoami` print system information. `ps` lists a process, and `>` saves that output to `process.log`.

```bash
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
```

**Input used:** `Raghavendra`, `24BCS10250`, `Learning Bash`

**Terminal output**

```text
Current date: Thu Aug 20 10:41:29 IST 2026
Hostname: Lingas-MacBook-Air.local
Username: lingaraghavendra
Process information saved to process.log
PID TTY           TIME COMM
14404 ??         0:00.00 bash
My name is Raghavendra
My roll number is 24BCS10250
My comment is: Learning Bash
```

The date and process ID change on every run.

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
