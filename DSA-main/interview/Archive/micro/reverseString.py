import re

def reverse_words(sentence):
    # Split the sentence into words and non-word characters
    parts = re.findall(r"[\w']+|[\W]+", sentence)

    # Reverse words and keep non-word characters unchanged
    reversed_parts = [part[::-1] if part.isalpha() else part for part in parts]

    # Join the reversed parts to form the reversed sentence
    reversed_sentence = ''.join(reversed_parts)

    return reversed_sentence

if __name__ == "__main__":
    # Example usage:
    sentence = "Hello, world! How are you doing today?"
    reversed_sentence = reverse_words(sentence)
    print(reversed_sentence)