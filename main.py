import ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10

from constants import paragraph, logs, temperatures


# Exercise 1
program1 = ex1.ex1([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
program1.run()

# Exercise 2 (Assuming that we should return every valid sublist)
program2 = ex2.ex2([1, 2, 1, 1, 3, 3, 2, 1, 3, 4, 1], 5)
program2.run()

# Exercise 3 (I gave example paragraph in constants.py that have more than 3 words with the same frequency)
program3_1 = ex3.ex3(paragraph)
program3_2 = ex3.ex3('Hello Hello Hello Hello World World World Example Example Test')
program3_1.run()
program3_2.run()

# # Exercise 4 (Assuming that we cannot have duplicate values)
program4 = ex4.ex4({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
program4.run()
# program4_error = ex4.ex4({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 5})
# program4_error.run()

# Exercise 5 (I'm not going to create a file for this, I think value from constants.py is enough)
# Also, I'm using \n as a delimiter for a string, it shouldn't be a list from the beggining
program5 = ex5.ex5(logs)
program5.run()

# Exercise 6 (I'm going not to use input for this (It's trivial), values for matrix are generated
# incrementally by 1 in top-bottom order just to have easy debugging. Also, I'm not going to use
# numpy for this due to the simplicity of methods in there)
# Example: |1, 4|    |1, 2, 3|
#          |2, 5| -> |4, 5, 6|
#          |3, 6|
# M - rows, N - columns
program6 = ex6.ex6(4, 3)
program6.run()

# Exercise 7 (I'm not going to use input for this for the ease of debugging)
program7 = ex7.ex7(5, 8)
program7.run()

# Exercise 8 (Dictionary will be in constants.py in form {City:Temperature}. I'm using int for values)
# Trivia - Cities are from Poland
program8 = ex8.ex8(temperatures)
program8.run()

# Exercise 9 (For fun I'm using an API for countries in Europe and generating csv in csv_write.py file)
program9 = ex9.ex9("capitals.csv")
program9.run()

# # Exercise 10
program10 = ex10.ex10(100)
program10.run()