original=[-5,-1,3,-6,7,-4,3,-6,-5,3,6,9,1]


def process_list(numbers):
    modified=numbers.copy()
    for i in numbers.copy():
        if i<0:
            modified.remove(i)
            # print(i)
    modified.append(0)
    modified.sort()
    print("Original: ", numbers)
    print("Result: ",modified)

process_list(original)


