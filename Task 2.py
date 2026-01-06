with open('output.txt', 'w') as fh:
    fh.write(input("Enter text to write to the file:") + "\n")
    print("Data successfully written to output.txt\n")

with open('output.txt', 'a') as fh:
    fh.write(input("Enter additional text to append:"))
    print("Data successfully appended\n")

with open('output.txt', 'r') as fh:
    print("Final content of output.txt:")
    print(fh.read())