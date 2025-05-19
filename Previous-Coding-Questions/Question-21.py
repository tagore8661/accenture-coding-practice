"""
Refueling Vehicles -

You are incharge of a convoy of N vehicles, each with fuel meter which shows 
the fuel present in each vehicle in litres. Each vehicles need to travel a distance 
of X kilometers. If the fuel becomes empty before reaching X kilometers the 
vehicle can refuel but the refueling will be of X litres and if the vehicles 
completes the X kilometers where fuel is left over then the extra fuel will be 
given to the next vehicle in the convoy. You must rearrange the convoy such 
that the vehicles take minimum refueling stops. 

Your task is to find and return an integer value representing the minimum 
number of refueling stops required by the convoy of vehicles.

Note:
   • The vehicles can go 1 kilometer in a single litre.
   • The refueling at any point of time will be for X litres only.

Input Specification:

Input1: An integer value X. representing the distance to be travelled.
Input2: An integer value N, representing the number of vehicles in the convoy.

Example1 :
   Input :
     X = 10  # Distance to travel
     N = 5   # Number of vehicles
     fuel_list = [5, 7, 12, 8, 15]  # Fuel in each vehicle

   Outpu: 1


Example2 :
   Input :
     X = 10
     N = 4
     fuel_list = [2, 3, 1, 6]

   Outpu: 4

"""

def min_refueling_stops(X, N, fuel_list):
    # Sort the vehicles based on their fuel levels in descending order
    fuel_list.sort(reverse=True)  #[15,12,8,7,5]
    
    # Initialize the count of refueling stops
    refueling_stops = 0
    leftover_fuel = 0
    
    # Iterate over each vehicle in the sorted list
    for fuel in fuel_list:
        # Add leftover fuel from previous vehicle (if any)
        fuel += leftover_fuel
        
        # If fuel is less than the distance X, refuel the vehicle
        if fuel < X:
            refueling_stops += 1
            fuel = X  # After refueling, the vehicle will have exactly X litres
        
        # Calculate leftover fuel after traveling X kilometers
        leftover_fuel = fuel - X
    
    return refueling_stops


# Example usage:
X = 10  # Distance to travel
N = 5   # Number of vehicles in the convoy
fuel_list = [5, 7, 12, 8, 15]  # Fuel in each vehicle

result = min_refueling_stops(X, N, fuel_list)
print(f"Minimum number of refueling stops: {result}")