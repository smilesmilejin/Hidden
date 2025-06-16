def hidden(matrix, n):
    # Your implementation here!
    # pass

    # flatten the matrix [] - loop through each row matrix and add it to the list
    # result_list = []
    # for loop to iterate thorugh flat matrix (0, len(matrix), n)
        # add the to resut list
    # use .join to return the result_list as string joined

    flat_matrix = []

    for row in matrix:
        flat_matrix.extend(row)

    print(flat_matrix)

    result_list = []
    for index in range(0, len(flat_matrix), n):
        result_list.append(flat_matrix[index])
    
    print(result_list)
    return ''.join(result_list)

# matrix_1 = (
#     ('u','e','r','e', ' ', 'e'),
#     ('d', 'z', 'o', 'b', 'i', 'v'),
#     ('n',),
#     ('w', 'g', 'q', ' ', '5', 'g', 'w'),
#     ('r',),
#     ('y', 'e'),
#     ('u', 'a', 'u', 't')
# )

# print(hidden(matrix_1, 2))


matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n',),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r',),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)
assert hidden(matrix_1, 2) == 'ur doing great'
assert hidden(matrix_1, 3) == 'uedbnqgya'
assert hidden(matrix_1, 525600) == 'u'
assert hidden(matrix_1, 1) == 'uere edzobivnwgq 5gwryeuaut'

matrix_2 = (
    ('💜',),
)
assert hidden(matrix_2, 17) == '💜'
assert hidden(matrix_2, 1) == '💜'

print("All tests passed! Discuss time and space complexity if time remains!")

