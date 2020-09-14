def histogram(numbers):
    for count in numbers:
        output = ''
        for n in range(count):
            output += 'x'
        print(output)
histogram([1, 1, 1, 1, 5])