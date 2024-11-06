import re

def word_frequence(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    frequency_dict={}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word,0)+ 1
    return frequency_dict

sentence = "this is betty, i told you about betty."
print(word_frequence(sentence))
