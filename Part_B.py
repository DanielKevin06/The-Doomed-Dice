def calculate_probabilities():
    probabilities = [[0] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            probabilities[i][j] = (i + 1) + (j + 1)
    total = sum(map(sum, probabilities))
    probabilities = [[val / total for val in row] for row in probabilities]
    return probabilities
def undoom_dice_challenge(die_a, die_b):
    original_probability_matrix = [[(i + 1) + (j + 1) for j in range(6)] for i in range(6)]
    total = sum(map(sum, original_probability_matrix))
    original_probability_matrix = [[val / total for val in row] for row in original_probability_matrix]
    new_die_a = [min(4, round(sum(original_probability_matrix[i][j] * face for j, face in enumerate(die_a)))) for i in range(6)]
    new_die_b = new_die_a.copy()
    return new_die_a, new_die_b
die_a = [1, 2, 3, 4, 5, 6]
die_b = die_a
new_die_a, new_die_b = undoom_dice_challenge(die_a, die_b)
print(f"Original Die A: {die_a}")
print(f"Original Die B: {die_b}")
print(f"New Die A: {new_die_a}")
print(f"New Die B: {new_die_b}")