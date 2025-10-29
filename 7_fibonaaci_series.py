# fibonaaci series
# ex:- 0,1,1,2,3,5,8,13,21,34

#inbuitl:-
n=15
fib = [0,1] +[0]*(n-2)
[fib.__setitem__(i,fib[i-1] + fib[i-2]) for i in range(2,n)]
print("fibonaci series")
print(fib)

#for loop:-
n=15
a,b = 0,1
print("fibonaci series")
for _ in range(n):
    print(a, end=" ")
    a,b =b, a+b