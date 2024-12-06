groups = {}

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
        size = len(word)
        if size in groups:
            # Avoid adding duplicate words
            if word not in groups[size]:
                groups[size].append(word)
        else:
            # Add the word to a new group
            groups[size] = [word]

    # Show the groups
    for size, group in sorted(groups.items()):
        print(f'{size}:  {group}')

