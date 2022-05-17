"""Solve a multiple knapsack problem using a MIP solver."""
from ortools.linear_solver import pywraplp

class CSPSolver:
    def __init__(self, vehiclemngnt, securelocationmngnt):
        self.vehiclemngnt = vehiclemngnt
        self.securelocationmngnt = securelocationmngnt
        self.vehicles = self.vehiclemngnt.list_of_vehicles_ny_nb_of_seats()
        self.securelocation = self.securelocationmngnt.list_of_securelocation_by_nb_of_person()

    
    def csp_solver(self):
        data = {}
        data['vehicles'] = self.vehicles
        #print(self.vehicles)
        data['num_items'] = len(data['vehicles'])
        data['all_items'] = range(data['num_items'])

        print(self.securelocation)
        data['rescuelocation'] = self.securelocation
        data['num_bins'] = len(data['rescuelocation'])
        data['all_bins'] = range(data['num_bins'])

        # Create the mip solver with the SCIP backend.
        solver = pywraplp.Solver.CreateSolver('SCIP')
        if solver is None:
            print('SCIP solver unavailable.')
            return

        # Variables.
        # x[i, b] = 1 if item i is packed in bin b.
        x = {}
        for i in data['all_items']:
            for b in data['all_bins']:
                x[i, b] = solver.BoolVar(f'x_{i}_{b}')

        # Constraints.
        # Each item is assigned to at most one bin.
        for i in data['all_items']:
            solver.Add(sum(x[i, b] for b in data['all_bins']) <= 1)

        # The amount packed in each bin cannot exceed its capacity.
        for b in data['all_bins']:
            solver.Add(
                sum(x[i, b] * data['vehicles'][i]
                    for i in data['all_items']) <= data['rescuelocation'][b])

        # Objective.
        # Maximize total value of packed items.
        objective = solver.Objective()
        for i in data['all_items']:
            for b in data['all_bins']:
                #objective.SetCoefficient(x[i, b], data['values'][i])
                objective.SetCoefficient(x[i, b], data['vehicles'][i])
        objective.SetMaximization()

        status = solver.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            #print(f'Total packed value: {objective.Value()}')
            total_weight = 0
            for b in data['all_bins']:
                print(f'Recuse Location: {self.securelocationmngnt.list_of_rescue_location[b].name}')
                bin_weight = 0
                #bin_value = 0
                for i in data['all_items']:
                    if x[i, b].solution_value() > 0:
                        print(
                            #f"Item {i} weight: {data['vehicles'][i]} value: {data['values'][i]}"
                            f"\t\t--{self.vehiclemngnt.list_of_vehicles()[i][0]} - Number of seats: {data['vehicles'][i]}"
                        )
                        bin_weight += data['vehicles'][i]
                        #bin_value += data['values'][i]
                print(f'Total nb of persons: {bin_weight}')
                #print(f'Packed bin value: {bin_value}\n')
                total_weight += bin_weight
            print(f'Total: {total_weight}')
        else:
            print('The problem does not have an optimal solution.')

