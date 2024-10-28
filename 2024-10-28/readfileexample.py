# f is a file object
f = open('data.dat')
# Read each line as text
for line in f:
    # Remove trailing newline character
    print(line.strip().rjust(50, '-'))
f.close() # Close the file
