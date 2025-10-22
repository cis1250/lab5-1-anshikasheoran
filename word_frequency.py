import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# Get sentence
def get_sentence():
    while True:
        sentence = input("Enter a sentence: ").strip()
        if is_sentence(sentence):
            return sentence
        else:
            print("Error: Sentence must start with a capital letter, end with '.', '?', or '!', and contain at least one word.")

# Calculate word frequencies
def calculate_frequencies(sentence):
    words_list = []
    frequencies = []

    # Remove ending punctuation
    sentence_clean = sentence[:-1]
    words = sentence_clean.split()

    for word in words:
        word = word.lower()  
        if word in words_list:
            index = words_list.index(word)
            frequencies[index] += 1
        else:
            words_list.append(word)
            frequencies.append(1)
    return words_list, frequencies

# Print word frequencies
def print_frequencies(words, frequencies):
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

# Main function to control flow
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)
