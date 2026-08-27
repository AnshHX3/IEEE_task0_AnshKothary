N=int(input("Enter a number: "))
list=[]
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
            break
    else: 
        return True

print(is_prime(7))

for i in range(1, N+1):
    if is_prime(i)==True:
        list.append(i)
print(list)

