def print_upper_words(words, must_start_with):
    """Print each word in uppercase, but only if it starts with one of the specified letters."""
    for word in words:
        if word[0].lower() in must_start_with:
            print(word.upper())

# Test the function with a set of letters
print_upper_words(['elephant', 'egg', 'tree', 'Python', 'apple', 'eagle'], {'e', 'p'})