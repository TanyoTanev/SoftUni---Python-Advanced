'''6. Truck Tour

Suppose there is a circle. There are N petrol pumps on that circle. Petrol pumps are numbered 0 to (N−1) (both inclusive).
You have two pieces of information corresponding to each of the petrol pump: (1) the amount of petrol that petrol pump will give, and
(2) the distance from that petrol pump to the next petrol pump (kilometers).
Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps.
Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps.
The truck will move one kilometer for each liter of the petrol.

Input
The first line will contain the value of N
The next N lines will contain a pair of integers each, i.e. the amount of petrol that petrol pump will give and the distance between that petrol pump
and the next petrol pump

Output
An integer which will be the smallest index of the petrol pump from which we can start the tour

Constraints
1 ≤ N ≤ 1000001
1 ≤ Amount of petrol, Distance ≤ 1000000000

Examples
Input
Output
Comments

3
1 5
10 3
3 4
1'''
from collections import deque

N = int(input())

gas_station = deque()
fuel = deque()
tank = 0

def lines (gas_station, fuel):
    line = input().split(' ')
    gas_station.append(int(line[1]))
    fuel.append(int(line[0]))

    return gas_station, fuel


[ lines(gas_station, fuel) for x in range(N)]

#print(gas_station)
#print(fuel)
i = 0
beggining = 0

while i < N:

    current_fuel = fuel.popleft()
    current_distance = gas_station.popleft()
    tank = tank + current_fuel - current_distance

    #if i == N:
    #    break

    if tank >= 0:
        i +=1
        #gas_station.append(current_distance)
        #fuel.append(current_fuel)

    else:
        i=0
        beggining +=1
        tank=0
    gas_station.append(current_distance)
    fuel.append(current_fuel)


#print(gas_station)
#print(fuel)

print(beggining)