import ex1
import ex2
import ex3
import ex4
import ex5
import ex6
import ex7
import ex8
import numpy as np

np.random.seed(42) # For reproducibility

# Exercise 1
program1 = ex1.ex1()
program1.run()

# Exercise 2
ex2_points_a = np.random.rand(5, 2)
ex2_points_b = np.random.rand(6, 2)
program2 = ex2.ex2(ex2_points_a, ex2_points_b)
program2.run()

# Exercise 3
matrix_size = 10
ex3_matrix = np.random.rand(matrix_size, matrix_size)
np.fill_diagonal(ex3_matrix, 1)
program3 = ex3.ex3(ex3_matrix)
program3.run()

# Exercise 4
ex4_upper_triangular_matrix = np.triu(np.random.randint(-5, 16, (5, 5)))
program4 = ex4.ex4(ex4_upper_triangular_matrix)
program4.run()

# Exercise 5
# I don't know why the result is equal to -142.2222..., not -128.3333...
# Do you have any guess?
ex5_vector = np.linspace(-7.5, 5.5, 40)
program5 = ex5.ex5(ex5_vector)
program5.run()

# Exercise 6
# Incommpatible system of equations
program6_incompatible = ex6.ex6([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3])
program6_incompatible.exercise_name = "ex 6 - Incompatible system of equations"
program6_incompatible.run()
# Compatible system of equations
program6 = ex6.ex6([[3, -1, 1], [1, 2, -10], [3, -1.5, 2]], [2, 1, 3])
program6.exercise_name = "ex 6 - Compatible system of equations"
program6.run()

# Exercise 7
ex7_vec1, ex7_vec2, ex7_vec3 = [-1, 0, 1], [1, 2, 1], [3, 4, 5]
program7 = ex7.ex7(ex7_vec1, ex7_vec2, ex7_vec3)
program7.run()

# Exercise 8
ex8_vector = np.random.rand(50)
program8 = ex8.ex8(ex8_vector)
program8.run()
