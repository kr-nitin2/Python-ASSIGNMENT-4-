with open('sample.txt', 'w') as fh:
    fh.write("This is a sample text file.\n"
             "It contains multiple lines.")

try:
    with open('sample.txt', 'r') as fh:
        print("Reading file content:")
        line_number = 1
        for line in fh:
            print(f"Line {line_number}: {line}")
            line_number += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")