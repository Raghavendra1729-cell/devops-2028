#!/usr/bin/env bash

mkdir -p data
printf '%s\n' "This is a log file." > data/app.log
cat data/app.log
printf '%s\n' "This is my file" > data/app.log
cat data/app.log
