#!/usr/bin/env bash

mkdir -p test
echo "This is file1" > test/app.log
echo "This is file2" >> test/app.log
cat test/app.log
