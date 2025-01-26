
'''
write a function that takes a sentence as input and returns a dictionary with words as keys and their frequency as values.
'''
def word_to_frequency():
    sentence = input("enter a sentence: ").split()
    wordfrequency = {}
    for w in sentence:
        if w in wordfrequency:
            wordfrequency[w] += 1
        else:
            wordfrequency[w] = 1 # frequency for the word appearing for the first time
    return wordfrequency

# Calling for the function
print(word_to_frequency())














