from pulp import *

problem = LpProblem("q4", LpMaximize)

A = LpVariable("A", 0, 1, LpInteger)
B = LpVariable("B", 0, 1, LpInteger)
C = LpVariable("C", 0, 1, LpInteger)
D = LpVariable("D", 0, 1, LpInteger)
E = LpVariable("E", 0, 1, LpInteger)
F = LpVariable("F", 0, 1, LpInteger)
w = LpVariable("Excess", 0, None, LpInteger)

weight = 6 * A + 7 * B + 4 * C + 9 * D + 3 * E + 8 * F

problem += (60 * A + 70 * B + 40 * C + 70 * D + 16 * E + 100 * F) - 15 * w, "Value of items"
problem += w >= weight - 20, "Excess"

problem.solve()

print("Status:", LpStatus[problem.status])

for v in problem.variables():

    print(v.name, "=", v.varValue)

print("Value of items:", value(problem.objective))