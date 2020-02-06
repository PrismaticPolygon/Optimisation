from pulp import *

problem = LpProblem("q3", LpMaximize)

# We have 10 gallons of cyan paint, 5 gallons of magenta paint, and 11 gallons of yellow paint.
# Cyan, magenta, and yellow paint can be mixed to create red, green, blue, or black paint.
# The value of a gallon of red paint is 10; green paint, 15; blue paint, 25; black paint, 25.

y_r = LpVariable("Amount of yellow paint used to make red paint", 0, None, LpInteger)
y_g = LpVariable("Amount of yellow paint used to make green paint", 0, None, LpInteger)
y_k = LpVariable("Amount of yellow paint used to make black paint", 0, None, LpInteger)

c_g = LpVariable("Amount of cyan paint used to make green paint", 0, None, LpInteger)
c_b = LpVariable("Amount of cyan paint used to make blue paint", 0, None, LpInteger)
c_k = LpVariable("Amount of cyan paint used to make black paint", 0, None, LpInteger)

m_r = LpVariable("Amount of magenta paint used to make red paint", 0, None, LpInteger)
m_b = LpVariable("Amount of magenta paint used to make blue paint", 0, None, LpInteger)
m_k = LpVariable("Amount of magenta paint used to make black paint", 0, None, LpInteger)

r = LpVariable("Red", 0)
g = LpVariable("Green", 0)
b = LpVariable("Blue", 0)
k = LpVariable("Black", 0)

# Enter objective function first
problem += 10 * r + 15 * g + 25 * b + 25 * k, "Value of paint produced"

# Constraints on the amount of each amount of paint
problem += y_r + y_g + y_k <= 11, "Yellow paint threshold"
problem += c_g + c_b + c_k <= 10, "Cyan paint threshold"
problem += m_b + m_k + m_r <= 5, "Magenta paint threshold"

problem += y_r + m_r == r, "Red mix volume"
problem += y_g + c_g == g, "Green mix volume"
problem += m_b + c_b == b, "Blue mix volume"
problem += c_k + m_k + y_k == k, "Black mix volume"

# Constraints maintaining ratios
problem += y_r == m_r, "Red paint ratio"
problem += y_g == c_g, "Green paint ratio"
problem += m_b == c_b, "Blue paint ratio"
problem += c_k == m_k, "Black paint ratio"
problem += m_k == y_k, "Black paint sd"

problem.solve()

print("Status:", LpStatus[problem.status])

for v in problem.variables():

    print(v.name, "=", v.varValue)

print("Value of paint:", value(problem.objective))