# sum of digits in list

#inbuilt:-
numbers = [12,34,5,100]
# o/p:-  1+2+3+4+5+1+0+0
total_sum = sum(int(digit) for num in numbers for digit in str(num))
print("sum of digits", total_sum)

#loop
numbers = [12,34,5,100,77]
total_sum = 0
for num in numbers:
    while num > 0:
        digits = num %10
        total_sum += digits
        num //= 10
print("total sum", total_sum)



