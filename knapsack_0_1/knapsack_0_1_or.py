# Solving the knapsack 0-1 problem using the Google OR-Tools MIP solver.
# The item values and weights are provided through input lists.

import numpy as np
from ortools.algorithms import pywrapknapsack_solver

def knapsack_0_1_or(values, weights, capacities):
	# Declare the solver
	solver = pywrapknapsack_solver.KnapsackSolver(
		pywrapknapsack_solver.KnapsackSolver.
		KNAPSACK_MULTIDIMENSION_CBC_MIP_SOLVER, 'knapsack_0_1')
	# Call the solver
	solver.Init(values, weights, capacities)
	computed_value = solver.Solve()
	packed_items = []
	packed_weights = []
	total_weight = 0
	print('Total value =', computed_value)
	for i in range(len(values)):
		if solver.BestSolutionContains(i):
			packed_items.append(i)
			packed_weights.append(weights[0][i])
			total_weight += weights[0][i]
	print('Total weight:', total_weight)
	print('Packed items:', packed_items)
	print('Packed_weights:', packed_weights)

# List of item values
v = [7, 2, 10, 4]
# List of item weights
w = [3, 6, 9, 5]
# Knapsack capacity
C = 15
# knapsack_0_1_or(v, [w], [C])
v, w = np.loadtxt("knapsack_dataset_xl.txt", dtype=int, unpack=True)
wl = []
for i in range(1, len(w)):
	wl.append(w[i])
knapsack_0_1_or(v[1:], [wl], [v[0]])
