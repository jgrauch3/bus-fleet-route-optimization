import pandas as pd
import numpy as np

# 1. Generate Mock Club Data (Matches ISYE Phase 1/2 requirements)
clubs = ['Anderson', 'Barksdale', 'Carrol', 'Chamblee', 'Draper', 'Harland', 'Mimms', 'Worley']
club_data = pd.DataFrame({
    'club': clubs,
    'students': np.random.randint(40, 100, size=len(clubs)),
    'original_buses_14': np.random.randint(0, 2, size=len(clubs)),
    'original_buses_66': np.random.randint(0, 2, size=len(clubs))
})
club_data.to_excel('club_data.xlsx', index=False)

# 2. Generate Mock Routing Solutions (78 feasible solutions)
routing_solutions = pd.DataFrame({
    'solution_id': range(1, 79),
    'club': np.random.choice(clubs, 78),
    'service_time': np.random.uniform(10, 30, 78),
    'bus_14': np.random.randint(0, 3, 78),
    'bus_15': np.random.randint(0, 3, 78),
    'bus_24': np.random.randint(0, 2, 78),
    'bus_30': np.random.randint(0, 2, 78),
    'bus_66': np.random.randint(0, 1, 78)
})
routing_solutions.to_csv('routing_solutions.csv', index=False)

print("Mock data generated: club_data.xlsx and routing_solutions.csv")
