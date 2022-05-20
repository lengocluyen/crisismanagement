"""Solve a multiple knapsack problem using a MIP solver."""
from ortools.linear_solver import pywraplp

class CSPSolver:
    def __init__(self, vehiclemngnt, securepointmngnt):
        self.vehiclemngnt = vehiclemngnt
        self.securepointmngnt = securepointmngnt
        self.vehicles = self.vehiclemngnt.list_of_vehicles_by_nb_of_seats()
        self.distance_estimes_to_secure_points = self.vehiclemngnt.list_of_vehicles_by_distance_to_secure_points()
        print("self.distances", self.distance_estimes_to_secure_points)
        self.securepoint = self.securepointmngnt.list_of_securepoint_by_nb_of_person()

    
    def find_min_distance(self, list_of_distances):
        result = 100000
        for item in list_of_distances:
            if item[0]<= result:
                result = item[0]
        return float(result)


    def csp_solver(self):
        data = {}
        data['vehicles'] = self.vehicles
        print(self.vehicles)
        data['distances'] = self.distance_estimes_to_secure_points
        print("data['distances'][0]:", data['distances'][0])
        print("len(data['vehicles']): ", len(data['vehicles']))
        print("len(data['distances']): ", len(data['distances']))
        assert len(data['vehicles']) == len(data['distances'])
        data['num_vehicles'] = len(data['vehicles'])
        data['all_vehicles'] = range(data['num_vehicles'])

        print(self.securepoint)
        data['securepoints'] = self.securepoint
        data['num_securepoints'] = len(data['securepoints'])
        data['all_securepoints'] = range(data['num_securepoints'])

        # Create the mip solver with the SCIP backend.
        solver = pywraplp.Solver.CreateSolver('SCIP')
        if solver is None:
            print('SCIP solver unavailable.')
            return

        # Variables.
        # x[i, b] = 1 if vehicle i is allocated for securepoint b.
        x = {}
        for i in data['all_vehicles']:
            for b in data['all_securepoints']:
                x[i, b] = solver.BoolVar(f'x_{i}_{b}')
        # Constraints.
        # Each vehilce is assigned to at most one securepoint.
        for i in data['all_vehicles']:
            solver.Add(sum(x[i, b] for b in data['all_securepoints']) <= 1)

        # The amount seat of vehicle allocated in each securepoint cannot exceed its total of persons .
        for b in data['all_securepoints']:
            solver.Add(
                sum(x[i, b] * data['vehicles'][i]
                    for i in data['all_vehicles']) >= data['securepoints'][b] + 3)
        
        # Objective.
        # Minimize total dstances from vehicles and secure points
        objective = solver.Objective()
        for i in data['all_vehicles']:
            for b in data['all_securepoints']:
                value = data['distances'][i]
                objective.SetCoefficient(x[i, b], float(value[b][0]))
        objective.SetMinimization()
        
        status = solver.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            print(f'Total distances: {objective.Value()}')
            total_vehicle_seats = 0
            for b in data['all_securepoints']:
                print(f'Recuse Point: {self.securepointmngnt.list_of_rescue_point[b].name}')
                total_person_of_securepoint = 0
                distance_vehicle_securepoint = 0
                for i in data['all_vehicles']:
                    if x[i, b].solution_value() > 0:
                        valueee = data['distances'][i]
                        print(
                            #f"Item {i} weight: {data['vehicles'][i]} value: {data['values'][i]}"
                            f"\t\t--{self.vehiclemngnt.list_of_vehicles()[i][0]} - Number of seats: {data['vehicles'][i]}, -Minimal Distance: {valueee[b][0]} in Distances: {valueee}"
                        )
                        total_person_of_securepoint += data['vehicles'][i]
                        distance_vehicle_securepoint += self.find_min_distance(data['distances'][i])
                print(f'Total nb of persons: {total_person_of_securepoint}')
                print(f'Minial Distance of Vehicle and Secure point : {distance_vehicle_securepoint}\n')
                total_vehicle_seats += total_person_of_securepoint
            print(f'Total: {total_vehicle_seats}')
        else:
            print('The problem does not have an optimal solution.')

