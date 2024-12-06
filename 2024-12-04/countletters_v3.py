# Initialize counting variables
letter_counts = {}

# Open the file for reading
with open('declaration.text', 'r') as f:
    # Read in content of the entire file
    content = f.read()
    # Uppercase the content
    content = content.upper()
    # Count each character A-Z
    for ch in content:
        if 'A' <= ch <= 'Z':
            if ch not in letter_counts:
                letter_counts[ch] = 1
            else:
                letter_counts[ch] += 1

    # Report the counts for each letter
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(f'{ch}:  {letter_counts[ch]}')

