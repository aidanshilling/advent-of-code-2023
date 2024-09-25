def parse_round(round):

    key = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    round = round.replace(',', '')
    round_split = round.lstrip().strip().split(' ')
    print(round)
    for i in range(0, len(round_split), 2):
        print(round_split)
        if int(round_split[i]) > key[round_split[i+1]]:
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
            print("{} - {}".format(id, rounds))
            for round in rounds.split(';'):
                print(round)
                if not parse_round(round):
                    bad_game = True
                    break
            if not bad_game:
                good_games.append(int(id))

        print(sum(good_games))
