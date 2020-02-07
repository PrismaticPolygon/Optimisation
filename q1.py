from pulp import *

print("MINIMISATION\n")

min_p = LpProblem("q1min", LpMinimize)

x_1 = LpVariable("x_1", 0, None, LpInteger)
x_2 = LpVariable("x_2", 0, None, LpInteger)

min_p += x_1 - 3 * x_2, "Minimisation"

min_p += x_1 - x_2 <= 1, "1"
min_p += x_1 - x_2 >= -1, "2"
min_p += 2 * x_1 - x_2 <= 3, "3"

min_p.solve()

print("Status:", LpStatus[min_p.status])

for v in min_p.variables():

    print(v.name, "=", v.varValue)

print("Value of items:", value(min_p.objective))

print("\nMAXIMISATION\n") # Unbounded. Yikes.

max_p = LpProblem("q1max", LpMaximize)

x1 = LpVariable("x1", 0, None, LpInteger)
x2 = LpVariable("x2", 0, None, LpInteger)

s1 = LpVariable("s1", 0, None, LpInteger)
s2 = LpVariable("s2", 0, None, LpInteger)
s3 = LpVariable("s3", 0, None, LpInteger)

max_p += -x1 + 3 * x2, "Maximisation"

max_p += x1 - x2 + s1 == 1, "1"
max_p += -x1 + x2 + s2 == 1, "2"
max_p += 2 * x1 - x2 + s3 == 3, "3"

max_p.solve()

print("Status:", LpStatus[max_p.status])

variables = max_p.variables()

for v in max_p.variables():

    print(v.name, "=", v.varValue)

print("Value of items:", variables[3].varValue - 3 * variables[4].varValue)

# So: my formulation is still correct. I just can't do the maths right! Which is frustrating.
# Okay. Let's try again. I must be missing something.