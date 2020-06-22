# import the library PuLP as p 
import pulp as p
  
# Set Up a LP Maximization Problem:
Lp_prob = p.LpProblem('Activity-Analysis_1', p.LpMaximize) # Here we named the Problem "Acitity-Analysis".
  
# Set Up Problem Variables: 
c = p.LpVariable("c", lowBound = 0) # "c" for chair
t = p.LpVariable("t", lowBound = 0) # "t" for table
d = p.LpVariable("d", lowBound = 0) # "d" for desk
b = p.LpVariable("b", lowBound = 0) # "b" for bookshelve

  
# Create Objective Function:
Lp_prob += 45 * c + 80 * t + 110 * d + 55 * b    
  
# Create Constraints: 
Lp_prob += 5 * c + 20 * t + 15 * d + 22 * b <= 20000
Lp_prob += 10 * c + 15 * t + 25 * d + 20 * b <= 4000
Lp_prob += 3 * c + 8 * t + 15 * d + 10 * b <= 2000
Lp_prob += 4 * c + 20 * d <= 3000
Lp_prob += 20 * b <= 500
  
# Show the problem:
print(Lp_prob) # note that it's shown in alphabetical order
  


### Simplifying the Problem and Solving it ###

# Generate a New LP Maximization Problem:
Lp_prob2 = p.LpProblem('Activity-Analysis_2', p.LpMaximize)
  
# Generate Problem Variables (>= 0): 
c = p.LpVariable("c", lowBound = 0)
t = p.LpVariable("t", lowBound = 0)


  
# Create Objective Function:
Lp_prob2 += 45 * c + 80 * t #+ 110 * d + 55 * b    
  
# Set Up the Constraints: 
Lp_prob2 += 5 * c + 20 * t <= 400
Lp_prob2 += 10 * c + 15 * t <= 450

  
# Show the problem:
print(Lp_prob2) # note that it's shown in alphabetical order
  
# Solve the Problem:
status = Lp_prob2.solve()
print(p.LpStatus[status])   # Display Solution Status 
  
# Printing the final solution 
print(p.value(c), p.value(t), p.value(Lp_prob2.objective)) 

# Printing Number of Chairs and Tables:
for var in (c,t):
    print('Optimal number of {} to produce is: {:1.0f}'
          .format(var.name, var.value()))

### END ###
