
# map {
#   name
#   lines = [
#       {source, dest, length}
#   ]
# }

def parse_input(input):
    result = {}
    with open(input, 'r') as f:
        contents = f.read()
        sections = contents.split("\n\n")
        for section in sections:
            name, data = section.split(':')
            if 'map' in name:
                data_map = create_map(name, data.split())
                result[name] = data_map
                continue
            # convert seed numbers into int's for consistency with maps
            result[name] = list(map(lambda x: int(x), data.split()))
    return result


def create_map(name, data):
    result = {'name': name, 'lines': []}
    for i in range(0, len(data), 3):
        result['lines'].append({
            'source': int(data[i+1]),
            'dest': int(data[i]),
            'length': int(data[i+2])
        })
    return result


def locate_seeds(almanac):
    seeds = almanac['seeds']
    result = {'location_list': [], 'location_map': []}
    for seed in seeds:
        val = seed
        for key in almanac:
            if key == 'seeds':
                continue
            for line in almanac[key]['lines']:
                source = line['source']
                dest = line['dest']
                length = line['length']

                # print(val, source, source + length)
                if val >= source and val < (source + length):
                    # print("{} {} - Found".format(seed, key))
                    dist = val - source
                    val = dest + dist
                    break
        result['location_map'].append({
            'seed': seed,
            'location': val
        })
        result['location_list'].append(val)
    return result


if __name__ == "__main__":
    almanac = parse_input('input')
    location_map = locate_seeds(almanac)

    answer1 = min(location_map['location_list'])
    print("P1 answer: {}".format(answer1))
