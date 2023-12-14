#!/bin/bash

# Find all test files
test_files=$(find . -name '*_test.c')

# Loop over each test file
for test_file in $test_files
do
    # Extract the base name of the file (without extension)
    base_name_test=$(basename $test_file .c)

    # Extract the base name of the test file (without '_test.c' extension)
    base_name_src=$(basename $test_file _test.c)

    # Form the source file name
    source_file="${base_name_src}.c"

    # Compile the test file, the source file, and the Unity framework
    gcc -fprofile-arcs -ftest-coverage -I ../Unity/ ../Unity/unity.c $source_file $test_file -o "${base_name_test}"
    # Run the test
    ./$base_name_test
done
pip install gcovr
gcovr --root . --html --html-details -o test_coverage.html
