from pulp import *

problem = LpProblem("q4", LpMaximize)

A = LpVariable("A", 0, 1, LpInteger)
B = LpVariable("B", 0, 1, LpInteger)
C = LpVariable("C", 0, 1, LpInteger)
D = LpVariable("D", 0, 1, LpInteger)
E = LpVariable("E", 0, 1, LpInteger)
F = LpVariable("F", 0, 1, LpInteger)

problem += 60 * A + 70 * B + 40 * C + 70 * D + 16 * E + 100 * F, "Value of items"

problem += 6 * A + 7 * B + 4 * C + 9 * D + 3 * E + 8 * F <= 20, "Weight"

problem.solve()

print("Status:", LpStatus[problem.status])

for v in problem.variables():

    print(v.name, "=", v.varValue)

print("Value of items:", value(problem.objective))