def parse_round(round):

    key = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    rolls = round.split(',')
    for roll in rolls:
        count, color = roll.lstrip().strip().split(' ')
        if int(count) > key[color]:
            return False
    return True


if __name__ == "__main__":
    with open('./input', 'r') as f:
        good_games = []
        for line in f:
            bad_game = False
            game = line.strip()
            id, rounds = game.split(':')
            id = id.split(' ')[1]
            for round in rounds.split(';'):
                if not parse_round(round):
                    bad_game = True
                    break
            if not bad_game:
                good_games.append(int(id))

        print("Part 1 answer: {}".format(sum(good_games)))
