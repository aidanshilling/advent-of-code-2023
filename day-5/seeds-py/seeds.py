
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


def resolve_map(map):
    result = {}
    for line in map['lines']:
        source = line['source']
        dest = line['dest']
        length = line['length']
        for i in range(0, length):
            result[source + i] = dest + i
    return result


def resolve_almanac(almanac):
    result = []
    for key in almanac:
        if key == 'seeds':
            continue
        m = resolve_map(almanac[key])
        result.append(m)
    return result


def locate_seeds(seeds, map_list):
    result = {'location_list': [], 'location_map': []}
    for seed in seeds:
        val = seed
        for m in map_list:
            val = m[val] if m.get(val) else val
        result['location_map'].append({
            'seed': seed,
            'location': val
        })
        result['location_list'].append(val)
    return result


if __name__ == "__main__":
    almanac = parse_input('input')
    map_list = resolve_almanac(almanac)
    location_map = locate_seeds(almanac['seeds'], map_list)

    answer1 = min(location_map['location_list'])
    print("P1 answer: {}".format(answer1))
