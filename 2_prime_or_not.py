# prime num or not

# inbuilt methods

num = 13
prime = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) +1))
print(f"{num} is prime" if prime else f"{num} is not prime")

# using for loop
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")
else:
    print(f"{num} is not prime")


# using list comprehension
divisors = [i for i in range(2, int(num**0.5) +1) if num % i ==0]
if num>1 and not divisors:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")

    



