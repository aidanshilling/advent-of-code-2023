def read_schematic_into_matrix(schematic):
    valid_digits = (
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
    )
    matrix = []
    symbols = {}
    numbers = []
    with open(schematic, 'r') as f:
        i = 0
        for line in f:
            row = []
            j = 0
            for char in line.strip():
                if char in valid_digits:
                    if len(numbers) > 0 and numbers[-1]['end']['j'] == j-1:
                        numbers[-1]['end'] = {'i': i, 'j': j}
                        numbers[-1]['value'] = numbers[-1]['value'] + char
                    else:
                        numbers.append({
                            'start': {'i': i, 'j': j},
                            'end': {'i': i, 'j': j},
                            'value': char
                        })
                elif char != '.':
                    symbols["({}, {})".format(i, j)] = True
                else:
                    symbols["({}, {})".format(i, j)] = False
                row.append(char)
                j += 1
            matrix.append(row)
            i += 1
    return matrix, numbers, symbols


def get_surrounding_coords(num, w, h):
    i = num['start']['i']
    j1 = num['start']['j']
    j2 = num['end']['j']

    coords = []
    if j1-1 >= 0:
        start = j1-1
        coords.append((i, j1-1))
    else:
        start = 0
    if j2+1 < w-1:
        stop = j2+2
        coords.append((i, j2+1))
    else:
        stop = w-1

    for x in range(start, stop):
        if i != 0:
            coords.append((i-1, x))
        if i < h-1:
            coords.append((i+1, x))

    return coords


def find_valid_part_numbers(matrix, numbers, symbols):

    # [i-1,j], [i+1,j], [i, j-1], [i, j+1],
    # [i-1, j-1], [i-1, j+1], [i+1, j-1], [i+1, j+1]
    good_numbers = []
    h = len(matrix)
    w = len(matrix[0])

    for num in numbers:
        # will need to account for being on the edges of the matrix
        # and when two numbers are next to eachother in the same row
        # (they would be part of the same number)
        coords = get_surrounding_coords(num, w, h)
        for coord in coords:
            if symbols["({}, {})".format(coord[0], coord[1])]:
                good_numbers.append(int(num['value']))

    return good_numbers


if __name__ == "__main__":

    matrix, numbers, symbols = read_schematic_into_matrix('input')
    good_numbers = find_valid_part_numbers(matrix, numbers, symbols)

    answer = sum(good_numbers)
    print("P1 Answer: {}".format(answer))
