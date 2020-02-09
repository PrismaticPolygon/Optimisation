from pulp import *

print("MAXIMISATION\n")

max_p = LpProblem("q1min", LpMaximize)

x_1 = LpVariable("x_1", 0, None, LpInteger)
x_2 = LpVariable("x_2", 0, None, LpInteger)
x_3 = LpVariable("x_3", 0, None, LpInteger)
x_4 = LpVariable("x_4", 0, None, LpInteger)
x_5 = LpVariable("x_5", 0, None, LpInteger)
x_6 = LpVariable("x_6", 0, None, LpInteger)

max_p += 2 * x_1 + x_2 - x_3, "Maximisation"

max_p += -2 * x_1 + x_2 + x_3 + x_4 == 1, "1"
max_p += x_1 - x_2 + x_5 == 2, "2"
max_p += 2 * x_1 - 3 * x_2 - x_3 + x_6 == 6, "3"

max_p.solve()

print("Status:", LpStatus[max_p.status])

for v in max_p.variables():

    print(v.name, "=", v.varValue)

print("Value of items:", value(max_p.objective))