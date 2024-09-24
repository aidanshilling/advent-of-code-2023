if __name__ == "__main__":
    with open('./input1', 'r') as f:
        number_s = {
            'one': "1",
            'two': "2",
            'three': "3",
            'four': "4",
            'five': "5",
            'six': "6",
            'seven': "7",
            'eight': "8",
            'nine': "9",
            'zero': "0"
        }
        number_i = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9"
        ]
        sums = []
        for line in f:
            digits = []
            line = line.strip()
            i = 0
            j = 0
            while i < len(line):
                if line[i] in number_i:
                    digits.append(line[i])
                    i += 1
                    continue
                s = line[i]
                j = i + 1
                while j < len(line):
                    if line[j] in number_i:
                        break
                    s += line[j]
                    if s in number_s.keys():
                        digits.append(number_s[s])
                    j += 1
                i += 1
            n = int(digits[0] + digits[len(digits)-1])
            print("{} - {}: {}".format(line, digits, n))
            sums.append(n)
        answer = sum(sums)
        print(answer)
