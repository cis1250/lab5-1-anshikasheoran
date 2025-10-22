import re
import string

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

def get_sentence():
    while True:
        sentence = input("Enter a sentence: ").strip()
        if is_sentence(sentence):
            return sentence
        else:
            print("Error: Sentence must start with a capital letter, end with '.', '?', or '!', and contain at least one word.")

def calculate_frequencies(sentence):
    words_list = []
    frequencies = []

    words = sentence.split()
    for word in words:
        # Remove punctuation from start and end of each word
        word_clean = word.strip(string.punctuation).lower()
        if word_clean:  # skip empty words
            if word_clean in words_list:
                index = words_list.index(word_clean)
                frequencies[index] += 1
            else:
                words_list.append(word_clean)
                frequencies.append(1)
    return words_list, frequencies

def count_punctuation(sentence):
    punctuation_count = {}
    for char in sentence:
        if char in string.punctuation:
            if char in punctuation_count:
                punctuation_count[char] += 1
            else:
                punctuation_count[char] = 1
    return punctuation_count

def print_frequencies(words, frequencies):
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

def print_punctuation(punctuation_count):
    print("\nPunctuation Counts:")
    for punc, count in punctuation_count.items():
        print(f"{punc}: {count}")

def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    punctuation_count = count_punctuation(sentence)

    print_frequencies(words, frequencies)
    print_punctuation(punctuation_count)

if __name__ == "__main__":
    main()
