
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
            map = create_map(data)
            result[name] = map


def create_map(data):
    None


def map_resolver(map):
    result = {}
    for line in map['lines']:

        source = line['source']
        dest = line['dest']
        length = line['length']

        for i in range(0, length):
            result[source + i] = dest + i
    return result


if __name__ == "__main__":
    parse_input('input-test')
    answer1 = 0
    print("P1 answer: {}".format(answer1))
