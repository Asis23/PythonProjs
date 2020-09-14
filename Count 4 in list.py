def count4 (numbers):
    count = 0
    for num in numbers:
        if num == 4:
            count = count + 1
    return count

print (count4 ([1,3,2,4,5,4,3,4,5,4,4,3,4,5]))