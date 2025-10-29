#count vowels in string

text = "i love python automation"
vowels = "aeiouAEIOU"

count = sum(1 for ch in text if ch in vowels)
print("number of vowels:", count)

# loop
text = "i love python automation manual also"
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1
print("number of vowels", count)


