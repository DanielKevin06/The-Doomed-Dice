total_combinations = 6 * 6
print(f'Total Combinations: {total_combinations}')

distribution_matrix = [[0] * 6 for _ in range(6)]

for i in range(6):
    for j in range(6):
        distribution_matrix[i][j] = (i + 1) + (j + 1)

print('Distribution Matrix:')
for row in distribution_matrix:
    print(row)

probability_matrix = [[count / total_combinations for count in row] for row in distribution_matrix]

print('Probability Matrix:')
for row in probability_matrix:
    print(row)