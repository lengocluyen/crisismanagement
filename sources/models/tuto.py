"""Solves a multiple knapsack problem using the CP-SAT solver."""
from ortools.sat.python import cp_model

def computing_nb_of_resource_and_capacity(vehicles_seats, securepoint_capacities):
    v1 = [0,0,0]
    v2 = [7,0,0]
    for i in range(len(vehicles_seats)):
        v1[0] += vehicles_seats[i][0]
        v1[1] += vehicles_seats[i][1]
        v1[2] += vehicles_seats[i][2]
    for i in range(len(securepoint_capacities)):
        v2[0] += securepoint_capacities[i][0]
        v2[1] += securepoint_capacities[i][1]
        v2[2] += securepoint_capacities[i][2]
    full_resource = v1[0] >= v2[0] and v1[1] >= v2[1] and v1[2] >= v2[2]
    return v1, v2, full_resource

def find_info_in_used_list(vehicles_i, distance_i, used_distance):
    for item in used_distance:
        if item[0][0] == vehicles_i[0] and item[0][1] == vehicles_i[1] and item[0][2] == vehicles_i[2]\
         and distance_i == item[1]:
            return 1
    return 0

def find_smallest_distance(vehicles_seats, distances,used_distance=[], index=0):
    assert(len(vehicles_seats) ==  len(distances))
    d = 1000000
    k = -1
    for i in range(len(distances)):
        not_find_info_in_used_list = find_info_in_used_list(vehicles_seats[i], distances[i], used_distance)
        if distances[i] <= d and vehicles_seats[i][index] > 0 and not_find_info_in_used_list == 0:
            k = i
            d = distances[k]
    if k is not -1:
        used_distance.append([vehicles_seats[k], distances[k]])
    return k, d, used_distance

def adding_resource_and_distance_by_reuse(vehicles_seats, distances, securepoint_capacities):
    v1, v2, _ = computing_nb_of_resource_and_capacity(vehicles_seats,securepoint_capacities)
    used_distance = []
    while v1[2] < v2[2]:
        i, d, used_distance = find_smallest_distance(vehicles_seats, distances,used_distance, index=2)
        vehicles_seats.append(vehicles_seats[i])
        d = d*5
        distances.append(d)
        v1, v2, _ = computing_nb_of_resource_and_capacity(vehicles_seats,securepoint_capacities)
    while v1[1] < v2[1] :
        i, d, used_distance = find_smallest_distance(vehicles_seats, distances,used_distance, index=1)
        vehicles_seats.append(vehicles_seats[i])
        d = d*5
        distances.append(d)
        v1, v2, _ = computing_nb_of_resource_and_capacity(vehicles_seats,securepoint_capacities)
    while v1[0] < v2[0]:
        i, d, used_distance = find_smallest_distance(vehicles_seats, distances,used_distance, index=0)
        vehicles_seats.append(vehicles_seats[i])
        d = d*5
        distances.append(d)
        v1, v2, _ = computing_nb_of_resource_and_capacity(vehicles_seats,securepoint_capacities)
    return vehicles_seats, distances, securepoint_capacities
            

def main():
    data = {}
    data['vehicle_seats'] = [
        [12, 10, 0], [20,5,5], [30,10,2], [36, 0, 0], [31, 4, 1], [45, 3, 0], [36, 2, 1]
    ]
    #[35, 5, 0], [36, 5, 2], [24, 0, 0], [30, 0 ,0], [30, 1, 1], [42, 1, 1], [36, 1, 1], [36, 0 ,0]
    data['distances'] = [
        10, 30, 25, 50, 35, 30, 15
    ]
    #, 40, 30, 35, 45, 10, 20, 30, 25

    data['securepoint_capacities'] = [[100, 10, 0], [45, 15, 0], [39, 0, 0], [28,5, 0], [70,10,0]]
    
    print("Original Resource:")
    print("data['vehicle_seats']:",data['vehicle_seats'])
    print("data['distances']: ", data['distances']) 
    print("data['securepoint_capacities']: ", data['securepoint_capacities'])
    _, _, full_resource =  computing_nb_of_resource_and_capacity(data['vehicle_seats'],data['securepoint_capacities'])
    print("full_resource: ", full_resource)
    if full_resource == False:
        data['vehicle_seats'], data['distances'],_ = adding_resource_and_distance_by_reuse(data['vehicle_seats'], data['distances'], data['securepoint_capacities'])
    
    print("enriching resource")
    print("data['vehicle_seats']:",data['vehicle_seats'])
    print("data['distances']: ", data['distances']) 
    print("data['securepoint_capacities']: ", data['securepoint_capacities'])
    _, _, full_resource =  computing_nb_of_resource_and_capacity(data['vehicle_seats'],data['securepoint_capacities'])
    print("full_resource: ", full_resource)
    

    assert len(data['vehicle_seats']) == len(data['distances'])
    data['num_items'] = len(data['vehicle_seats'])
    data['all_items'] = range(data['num_items'])
    data['num_securepoint'] = len(data['securepoint_capacities'])
    data['all_securepoint'] = range(data['num_securepoint'])


    model = cp_model.CpModel()

    # Variables.
    # x[i, b] = 1 if item i is packed in bin b.
    x = {}
    for i in data['all_items']:
        for b in data['all_securepoint']:
            x[i, b] = model.NewBoolVar(f'x_{i}_{b}')

    # Constraints.
    # Each item is assigned to at most one bin.
    for i in data['all_items']:
        model.AddAtMostOne(x[i, b] for b in data['all_securepoint'])

    # The amount packed in each bin cannot exceed its capacity.
    for b in data['all_securepoint']:
        model.Add(
            sum(x[i, b] * data['vehicle_seats'][i][0]
                for i in data['all_items']) >= data['securepoint_capacities'][b][0])
        model.Add(
            sum(x[i, b] * data['vehicle_seats'][i][1]
                for i in data['all_items']) >= data['securepoint_capacities'][b][1])
        model.Add(
            sum(x[i, b] * data['vehicle_seats'][i][2]
                for i in data['all_items']) >= data['securepoint_capacities'][b][2])
    # Objective.
    # Maximize total value of packed items.
    objective = []
    for i in data['all_items']:
        for b in data['all_securepoint']:
            objective.append(
                cp_model.LinearExpr.Term(x[i, b], data['distances'][i]))
    model.Minimize(cp_model.LinearExpr.Sum(objective))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        print(f'Total packed value: {solver.ObjectiveValue()}')
        total_vehicle_seats = [0,0,0]
        for b in data['all_securepoint']:
            print(f'securepoint {b}')
            securepoint_vehicle_seats = [0,0,0]
            securepoint_distances = 0
            for i in data['all_items']:
                if solver.Value(x[i, b]) > 0:
                    print(
                        f"Item {i} vehicle_seats: {data['vehicle_seats'][i]} distances: {data['distances'][i]}"
                    )
                    securepoint_vehicle_seats[0] += data['vehicle_seats'][i][0]
                    securepoint_vehicle_seats[1] += data['vehicle_seats'][i][1]
                    securepoint_vehicle_seats[2] += data['vehicle_seats'][i][2]
                    securepoint_distances += data['distances'][i]
            print(f'Packed securepoint vehicle_seats: {securepoint_vehicle_seats}')
            print(f'Packed securepoint value: {securepoint_distances}\n')
            total_vehicle_seats[0] += securepoint_vehicle_seats[0]
            total_vehicle_seats[1] += securepoint_vehicle_seats[1]
            total_vehicle_seats[2] += securepoint_vehicle_seats[2]
        print(f'Total packed vehicle_seats: {total_vehicle_seats}')
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()