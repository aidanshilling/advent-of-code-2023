def process_card(card):
    winning, actual = card['numbers'].split('|')
    winning = winning.split()
    actual = actual.split()

    result = {'inc': 0}
    idx = int(card['id'])
    matches = 0
    for num in actual:
        if num in winning:
            matches += 1
    for i in range(idx+1, idx+matches+1):
        inc = 1 * (card['count'] + 1)
        result['inc'] += inc
        result[str(i)] = inc

    return result


def process_card_stack():
    total_cards = 0
    copy_index = {}
    with open('input-test', 'r') as f:
        for line in f:
            total_cards += 1
            card, numbers = line.strip().lstrip().split(':')
            id = card.split()[1]
            copies = process_card({
                'id': id,
                'numbers': numbers,
                'count': copy_index[id] if copy_index.get(id) else 0
            })
            total_cards += copies['inc']
            for k, v in copies.items():
                if copy_index.get(k):
                    copy_index[k] += v
                else:
                    copy_index[k] = v
            print(id, copy_index)
    print(total_cards)


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
    process_card_stack()

    answer1 = total
    print("P1 Answer: {}".format(answer1))
