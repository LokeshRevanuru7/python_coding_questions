# check string is palindrome or not
# madam       -> palindorme
# hello          -> not palindrome


# inbuilt
string = "Madam"

if string == string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")


# for loop
string1 = "Madam"
reversed_str = ""

for char in string1:
    reversed_str = char + reversed_str

if string == reversed_str:
    print(f"{string1} is a palindrome")
else:
    print(f"{string1} is not a palindrome")
