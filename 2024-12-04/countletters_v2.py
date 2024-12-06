# Initialize counting variables
letter_counts = [0 for _ in range(26)]

# Open the file for reading
with open('declaration.text', 'r') as f:
    # Read in content of the entire file
    content = f.read()
    # Uppercase the content
    content = content.upper()
    # Count each character A-Z
    for ch in content:
        if 'A' <= ch <= 'Z':
            letter_counts[ord(ch) - 65] += 1

    # Report the counts for each letter
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(f'{ch}:  {letter_counts[ord(ch) - 65]}')

