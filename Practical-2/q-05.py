# Write a program to check given number of is prime or not.
lv = (int(input("Enter lower number of prime number : ")))
uv = (int(input("Enter upper number of prime number : ")))
for num in range(lv,uv+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print("Prime number ",num)