N=int(input("Enter the number of elements: "))
list=[]
sum=0
even_count=0
odd_count=0
reverse_list = []


for i in range(N):
    user_input = int(input("Enter a number:"))
    list.append(user_input)

largest=list[0]
smallest=list[0]

for i in range(1,len(list)):
    if list[i]>largest:
        largest=list[i]
    if list[i]<smallest:
        smallest=list[i]


for i in range(len(list)):
    sum+=list[i]
    if list[i]%2==0:
        even_count+=1
    else:
        odd_count+=1
    reverse_list.insert(0,list[i])


print("Largest: "+str(largest))
print("Smallest: "+str(smallest))
print("Sum: " + str(sum))
print("Even count: "+str(even_count))
print("Odd count: "+str(odd_count))
print("Reversed: " + str(reverse_list))

