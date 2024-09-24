with open('./input1', 'r') as f:
    numbers = [
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
    ]
    sums = []
    for line in f:
        line = line.strip()
        digits = []
        for c in line:
            if c in numbers:
                digits.append(c)
        combined = int(digits[0] + digits[len(digits)-1])
        print("{} - {}: {}".format(line, digits, combined))
        sums.append(combined)
    print(sum(sums))
