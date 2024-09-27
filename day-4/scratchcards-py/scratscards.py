
def get_full_total():
    total = 0
    with open('input', 'r') as f:
        for line in f:
            points = 0
            winning, actual = line.strip().lstrip().split(':')[1].split('|')
            winning = winning.split()
            actual = actual.split()
            for num in actual:
                if num in winning and points == 0:
                    points += 1
                elif num in winning:
                    points *= 2
            total += points
    return total


if __name__ == "__main__":

    total = get_full_total()

    answer1 = total
    print("P1 Answer: {}".format(answer1))
