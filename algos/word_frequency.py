import string

def word_frequency(sentence):
    # Remove punctuation and convert the sentence to lowercase
    translator = str.maketrans('', '', string.punctuation)
    sentence = sentence.translate(translator).lower()

    # Split the sentence into words
    words = sentence.split()

    # Create a dictionary to store word frequencies
    word_freq = {}

    # Count word frequencies
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
