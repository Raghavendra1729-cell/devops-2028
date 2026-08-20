#!/usr/bin/env bash

mkdir -p hello
printf '%s\n' "This is my logfile" > hello/app.log
cat hello/app.log
