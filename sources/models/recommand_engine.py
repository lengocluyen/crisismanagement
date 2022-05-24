"""Solve a multiple knapsack problem using a MIP solver."""
from ortools.linear_solver import pywraplp
#from ortools.sat.python import cp_model

class RecommandEngine:
    def __init__(self, vehiclemngnt, securepointmngnt):
        self.vehiclemngnt = vehiclemngnt
        self.securepointmngnt = securepointmngnt
        self.vehicles = self.vehiclemngnt.list_of_vehicles_by_nb_of_seats()
        self.distance_estimes_to_secure_points = self.vehiclemngnt.list_of_vehicles_by_distance_to_secure_points()
        #print("self.distances", self.distance_estimes_to_secure_points)
        self.securepoint = self.securepointmngnt.list_of_securepoint_by_nb_of_person()
        
        # initial data
        self.data = {}
        self.data['vehicle_seats'] = self.vehicles
        self.data['distances'] = self.distance_estimes_to_secure_points
        self.data['securepoint_capacities'] = self.securepoint

        assert len(self.data['vehicle_seats']) == len(self.data['distances'])
        self.data['num_items'] = len(self.data['vehicle_seats'])
        self.data['all_items'] = range(self.data['num_items'])
        self.data['num_securepoint'] = len(self.data['securepoint_capacities'])
        self.data['all_securepoint'] = range(self.data['num_securepoint'])



    
    def find_min_distance(self, list_of_distances):
        result = 100000
        for item in list_of_distances:
            if item[0]<= result:
                result = item[0]
        return float(result)

    def computing_nb_of_resource_and_capacity(self, vehicles_seats, securepoint_capacities):
        v1 = [0,0]
        v2 = [7,0]
        for i in range(len(vehicles_seats)):
            v1[0] += vehicles_seats[i][0]
            v1[1] += vehicles_seats[i][1]
            #v1[2] += vehicles_seats[i][2]
        for i in range(len(securepoint_capacities)):
            v2[0] += securepoint_capacities[i][0]
            v2[1] += securepoint_capacities[i][1]
            #v2[2] += securepoint_capacities[i][2]
        #full_resource = v1[0] >= v2[0] and v1[1] >= v2[1] and v1[2] >= v2[2]
        full_resource = v1[0] >= v2[0] and v1[1] >= v2[1]
        return v1, v2, full_resource

    def find_info_in_used_list(self, vehicles_i, distance_i, used_distance):
        for item in used_distance:
            if item[0][0] == vehicles_i[0] and item[0][1] == vehicles_i[1] \
            and distance_i == item[1]:
                return 1
        return 0

    def find_smallest_distance(self, vehicles_seats, distances,used_distance=[], index=0):
        assert(len(vehicles_seats) ==  len(distances))
        d = 1000000
        k = -1
        for i in range(len(distances)):
            not_find_info_in_used_list = self.find_info_in_used_list(vehicles_seats[i], distances[i], used_distance)
            if distances[i] <= d and vehicles_seats[i][index] > 0 and not_find_info_in_used_list == 0:
                k = i
                d = distances[k]
        if k is not -1:
            used_distance.append([vehicles_seats[k], distances[k]])
        return k, d, used_distance

    def adding_resource_and_distance_by_reuse(self, vehicles_seats, distances, securepoint_capacities):
        v1, v2, _ = self.computing_nb_of_resource_and_capacity(vehicles_seats,securepoint_capacities)
        used_distance = []
        while v1[1] < v2[1] :
            i, d, used_distance = self.find_smallest_distance(vehicles_seats, distances,used_distance, index=1)
            vehicles_seats.append(vehicles_seats[i])
            # hypothese that distance of resource will be multiplied by 5 for each time: it is reused
            d = d*5
            distances.append(d)
            v1, v2, _ = self.computing_nb_of_resource_and_capacity(vehicles_seats,securepoint_capacities)
        while v1[0] < v2[0]:
            i, d, used_distance = self.find_smallest_distance(vehicles_seats, distances,used_distance, index=0)
            vehicles_seats.append(vehicles_seats[i])
            d = d*5
            distances.append(d)
            v1, v2, _ = self.computing_nb_of_resource_and_capacity(vehicles_seats,securepoint_capacities)
        return vehicles_seats, distances, securepoint_capacities

    def generating_recommand(self, dynamic_resource=False):
        if dynamic_resource:
            _, _, full_resource =  self.computing_nb_of_resource_and_capacity(self.data['vehicle_seats'],self.data['securepoint_capacities'])
            if full_resource == False:
                self.data['vehicle_seats'], self.data['distances'],_ = self.adding_resource_and_distance_by_reuse(self.data['vehicle_seats'], self.data['distances'], self.data['securepoint_capacities'])
                print("Current Vehicle Resources aren't enough. The reuse of resources are allocated based on distance or time")
            else:
                print("Current Vehicle Resources can be allocated to all secure points")
        

        # Create the mip solver with the SCIP backend.
        solver = pywraplp.Solver.CreateSolver('SCIP')
        if solver is None:
            print('SCIP solver unavailable.')
            return
        # Variables.
        # x[i, b] = 1 if vehicle i is allocated for securepoint b.
        x = {}
        for i in self.data['all_items']:
            for b in self.data['all_securepoint']:
                x[i, b] = solver.BoolVar(f'x_{i}_{b}')

        # Constraints.
        # Each vehilce is assigned to at most one securepoint.
        for i in self.data['all_items']:
            solver.Add(sum(x[i, b] for b in self.data['all_securepoint']) <= 1)

        # The amount seat of vehicle allocated in each securepoint cannot exceed its total of persons . (plus )
        for b in self.data['all_securepoint']:
            solver.Add(
                sum(x[i, b] * self.data['vehicle_seats'][i][0]
                    for i in self.data['all_items']) >= self.data['securepoint_capacities'][b][0])
            solver.Add(
                sum(x[i, b] * self.data['vehicle_seats'][i][1]
                    for i in self.data['all_items']) >= self.data['securepoint_capacities'][b][1])
        
        # Objective.
        # Minimize total dstances from vehicles and secure points
        objective = solver.Objective()
        for i in self.data['all_items']:
            for b in self.data['all_securepoint']:
                value = self.data['distances'][i]
                objective.SetCoefficient(x[i, b], float(value[b][0]))
        objective.SetMinimization()
        return solver, x, objective

    def best_optimal_recommand(self, generateur, x, objective):
        status = generateur.Solve()
        if status == pywraplp.Solver.OPTIMAL:
            print(f'Total distances: {objective.Value()}')
            total_vehicle_seats = [0,0]
            for b in self.data['all_securepoint']:
                print(f'Recuse Point: {self.securepointmngnt.list_of_rescue_point[b].name}')
                total_person_of_securepoint = [0,0]
                distance_vehicle_securepoint = 0
                for i in self.data['all_items']:
                    if x[i, b].solution_value() > 0:
                        valueee = self.data['distances'][i]
                        print(
                            f"\t\t--{self.vehiclemngnt.list_of_vehicles()[i][0]} - Number of seats: {self.data['vehicle_seats'][i]}, -Minimal Distance: {valueee[b][0]}"
                        )
                        total_person_of_securepoint[0] += self.data['vehicle_seats'][i][0]
                        total_person_of_securepoint[1] += self.data['vehicle_seats'][i][1]
                        distance_vehicle_securepoint += self.find_min_distance(self.data['distances'][i])
                print(f'Total nb of persons: {total_person_of_securepoint}')
                print(f'Minial Distance of Vehicle and Secure point : {distance_vehicle_securepoint}\n')
                total_vehicle_seats[0] += total_person_of_securepoint[0]
                total_vehicle_seats[1] += total_person_of_securepoint[1]
            print(f'Total: {total_vehicle_seats}')
        else:
            print('The problem does not have an optimal solution.')


    def vehicle_resource_recommand(self, generateur, x, objective,  nb_of_recommend):
        k = 0
        status = generateur.Solve()
        while generateur.NextSolution() and k < nb_of_recommend:
            print("Vehicle Resources are allocated for secure points: ", (nb_of_recommend + 1))
            k = k + 1
            print(f'Total distances: {objective.Value()}')
            total_vehicle_seats = [0,0]
            for b in self.data['all_securepoint']:
                print(f'Recuse Point: {self.securepointmngnt.list_of_rescue_point[b].name}')
                total_person_of_securepoint = [0,0]
                distance_vehicle_securepoint = 0
                for i in self.data['all_items']:
                    if x[i, b].solution_value() > 0:
                        valueee = self.data['distances'][i]
                        print(
                            f"\t\t--{self.vehiclemngnt.list_of_vehicles()[i][0]} - Number of seats: {self.data['vehicle_seats'][i]}, -Minimal Distance: {valueee[b][0]}"
                        )
                        total_person_of_securepoint[0] += self.data['vehicle_seats'][i][0]
                        total_person_of_securepoint[1] += self.data['vehicle_seats'][i][1]
                        distance_vehicle_securepoint += self.find_min_distance(self.data['distances'][i])
                print(f'Total nb of persons: {total_person_of_securepoint}')
                print(f'Minial Distance of Vehicle and Secure point : {distance_vehicle_securepoint}\n')
                total_vehicle_seats[0] += total_person_of_securepoint[0]
                total_vehicle_seats[1] += total_person_of_securepoint[1]
            print(f'Total: {total_vehicle_seats}')
        else:
            print('The problem does not have an optimal solution.')
"""
    def csp_solver_SCIP(self):
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

        # The amount seat of vehicle allocated in each securepoint cannot exceed its total of persons . (plus )
        for b in data['all_securepoints']:
            solver.Add(
                sum(x[i, b] * data['vehicles'][i]
                    for i in data['all_vehicles']) >= data['securepoints'][b])
        
        # Objective.
        # Minimize total dstances from vehicles and secure points
        objective = solver.Objective()
        for i in data['all_vehicles']:
            for b in data['all_securepoints']:
                value = data['distances'][i]
                objective.SetCoefficient(x[i, b], float(value[b][0]))
        objective.SetMinimization()
        
        status = solver.Solve()
        k = 0
        if status == pywraplp.Solver.OPTIMAL:
        #while solver.NextSolution() and k < 5:
            print('k: ', k)
            k = k + 1
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

"""