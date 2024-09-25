def check_round_validity(round):
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


def check_game_validity(rounds):
    for round in rounds.split(';'):
        if not check_round_validity(round):
            return False
    return True


def get_round_min(round):
    rolls = round.split(',')
    min = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for roll in rolls:
        count, color = roll.lstrip().strip().split(' ')
        min[color] += int(count)
    return min


def get_game_min(rounds):
    min = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for round in rounds.split(';'):
        round_min = get_round_min(round)
        if min['red'] < round_min['red']:
            min['red'] = round_min['red']
        if min['green'] < round_min['green']:
            min['green'] = round_min['green']
        if min['blue'] < round_min['blue']:
            min['blue'] = round_min['blue']
    return min


def get_power_set(d):
    return d['red'] * d['green'] * d['blue']


if __name__ == "__main__":
    with open('./input', 'r') as f:
        good_games = []
        power_sets = []
        for line in f:
            game = line.strip()
            id, rounds = game.split(':')
            id = id.split(' ')[1]
            if check_game_validity(rounds):
                good_games.append(int(id))
            game_min = get_game_min(rounds)
            power_sets.append(get_power_set(game_min))
        print("Part 1 answer: {}".format(sum(good_games)))
        print("Part 2 answer: {}".format(sum(power_sets)))

