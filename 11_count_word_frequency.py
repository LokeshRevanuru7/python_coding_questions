 # count word frequency in string

#inbuilt:-
from collections import Counter
text = "python is easy and python is automation"
words = text.split() 
word_freq = Counter(words)
print(word_freq)


#for loop
text1 = "python is easy and python also is automation and Api testing"
words  = text1.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] +=1
    else:
        word_freq[word] =1
print("text1 of", word_freq)



