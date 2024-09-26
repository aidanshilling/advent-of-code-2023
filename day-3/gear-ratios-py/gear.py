def read_schematic_into_matrix(schematic):
    invalid_symbols = (
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
        '.'
    )
    matrix = []
    symbols = []
    with open(schematic, 'r') as f:
        i = 0
        for line in f:
            row = []
            j = 0
            for char in line.strip():
                if char not in invalid_symbols:
                    symbols.append((i, j))
                row.append(char)
                j += 1
            matrix.append(row)
            i += 1
    return matrix, symbols


def find_valid_part_numbers(matrix, symbols):

    numbers = (
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

    # [i-1,j], [i+1,j], [i, j-1], [i, j+1],
    # [i-1, j-1], [i-1, j+1], [i+1, j-1], [i+1, j+1]

    for (i, j) in symbols:
        # will need to account for being on the edges of the matrix
        # and when two numbers are next to eachother in the same row
        # (they would be part of the same number)
        print(matrix[i][j])


if __name__ == "__main__":

    matrix, symbols = read_schematic_into_matrix('input')
    find_valid_part_numbers(matrix, symbols)

    answer = 0
    print("P1 Answer: {}".format(0))
