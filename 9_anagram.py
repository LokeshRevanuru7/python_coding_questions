# anagram
# ex:- listen   -> silent     -> anagram
#         hello   -> world      -> not anagram
from os import MFD_ALLOW_SEALING

#inbuilt:-
str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("it's anagram")
else:
    print("it's not anagram")


# loop
str1 = "listen"
str2 = "hello"
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if len(str1) != len(str2):
    print("it's not anagram")
else:
    is_anagram = True
    for ch in str1:
        if str1.count(ch) != str2.count(ch):
            is_anagram = False
            break
    print("Anagram" if is_anagram else "not anagram")
