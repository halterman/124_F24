word_counts = {}

# Open the file for reading
with open('declaration.text', 'r') as f:
    # Read in content of the entire file
    content = f.read()
    # Uppercase the content
    content = content.upper()
    # Split into a list of words
    words = content.split()
    # Count each word
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    # Report the counts for each word
    for word, count in word_counts.items():
        print(f'{word}:  {count}')

