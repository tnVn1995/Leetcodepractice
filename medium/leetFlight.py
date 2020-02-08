from typing import List
def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    bookings = sorted(bookings, key=lambda x: x[0])
    flights_no = {x: y for x, y in zip(range(1, bookings[-1][1] + 1), bookings[-1][1] * [0])}
    for idx, val in enumerate(bookings):
        # print('The range is:\t', range(val[0], ranges+1))
        for flight in range(val[0], val[1] + 1):
            # print(f'Add {val[2]} seats to flight {flight}')
            flights_no[flight] += val[2]
    seats_per_flight = list(flights_no.items())
    seats = [x[1] for x in seats_per_flight[:n]]
    return seats
##

def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    bookings = sorted(bookings, key = lambda x: x[1])
    flights_no = {x:y for x,y in zip(range(1,bookings[-1][1]+1), bookings[-1][1]*[0])}
    for idx, val in enumerate(bookings):
        # print('The range is:\t', range(val[0], ranges+1))
        for flight in range(val[0], val[1]+1):
            # print(f'Add {val[2]} seats to flight {flight}')
            flights_no[flight] += val[2]
    seats_per_flight = list(flights_no.items())
    seats = [x[1] for x in seats_per_flight[:n]]
    if len(seats) - n == 0:
        return seats
    else:
        return seats + [0]*(n - len(seats))
bookings = [[2,2,50],[1,1,35],[3,3,40],[1,4,50]]

n = 4

corpFlightBookings(bookings,n)

res = [0] * (n + 1)

for start, end, seats in bookings:
    res[start - 1] += seats
    res[end] -= seats

s = 0
for index, i in enumerate(res):
    print('add',s,sep=' ')
    res[index] += s
    s += i
return res[:-1]
### Leet 2

res = []
nums = [1,2,3,4]
for idx in range(0,len(nums),2):
    # print(idx)
    # print([nums[idx + 1]] * nums[idx])
    res = res + [nums[idx + 1]] * nums[idx]

import numpy as np
X = np.array([[2,-1,-1]]).T