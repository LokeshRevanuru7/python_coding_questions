# find letter frequency in string

#inbuit:-
from collections import Counter

text = "hello world"
letter_freq = Counter(text)
print(letter_freq)



# for loop
text = "hello world"
letter_freq = {}
for ch in text:
    if ch in letter_freq:
        letter_freq[ch] +=1
    else:
        letter_freq[ch] =1
print(letter_freq)