# Write your solution for 1.4 here!
def is_prime(x):
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                print(x,"is not a prime number")
                print(i,"times",x//i,"is",x)
            else:
                print(x,"is not a prime number")
is_prime(5)
