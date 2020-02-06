from pulp import *

problem = LpProblem("q3", LpMaximize)

y_r = LpVariable("Amount of yellow paint used to make red paint", 0, None, LpInteger)
y_g = LpVariable("Amount of yellow paint used to make green paint", 0, None, LpInteger)
y_k = LpVariable("Amount of yellow paint used to make black paint", 0, None, LpInteger)

c_g = LpVariable("Amount of cyan paint used to make green paint", 0, None, LpInteger)
c_b = LpVariable("Amount of cyan paint used to make blue paint", 0, None, LpInteger)
c_k = LpVariable("Amount of cyan paint used to make black paint", 0, None, LpInteger)

m_r = LpVariable("Amount of magenta paint used to make red paint", 0, None, LpInteger)
m_b = LpVariable("Amount of magenta paint used to make blue paint", 0, None, LpInteger)
m_k = LpVariable("Amount of magenta paint used to make black paint", 0, None, LpInteger)

red   = (y_r + m_r) / 2
green = (y_g + c_g) / 2
blue  = (m_b + c_b) / 2
black = (c_k + m_k + y_k) / 3

# Enter objective function first
problem += 10 * red + 15 * green + 25 * blue + 25 * black, "Value of paint produced"

# Constraints on the amount of each amount of paint
problem += y_r + y_g + y_k <= 11, "Yellow paint threshold"
problem += c_g + c_b + c_k <= 10, "Cyan paint threshold"
problem += m_b + m_k + m_r <= 5, "Magenta paint threshold"

# Constraints maintaining ratios
problem += y_r == m_r, "Red paint ratio"
problem += y_g == c_g, "Green paint ratio"
problem += m_b == c_b, "Blue paint ratio"
problem += c_k == m_k == y_k, "Black paint ratio"

problem.solve()

print("Status:", LpStatus[problem.status])

for v in problem.variables():

    print(v.name, "=", v.varValue)

print("Value of paint:", value(problem.objective))