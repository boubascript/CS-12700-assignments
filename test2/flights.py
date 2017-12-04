import random as r
airports = ['LGA','SFO','SEA','DTW','EWR','ATL','ORD',
            'LAX','JFK','BOS','DCA']

sample_routes = {'LAX': ['SFO', 'ATL'],
                 'BOS': ['SFO', 'SEA'],
                 'SFO': ['JFK', 'BOS', 'BOS'],
                 'LGA': ['ATL', 'BOS'], 
                 'JFK': ['DCA', 'SFO'],
                 'ATL': ['SFO', 'SFO', 'DCA'],
                 'ORD': ['LAX', 'SFO'],
                 'DTW': ['BOS', 'LAX', 'JFK'], 
                 'DCA': ['SEA', 'SFO', 'LGA'], 
                 'SEA': ['DTW', 'SFO', 'LAX'], 
                 'EWR': ['SFO', 'ATL', 'SFO']}
                 
def create_routes(airports):
  flights = {}
  for airport in airports:
    otherports = list(airports)
    otherports.remove(airport)
    numdestinations = r.randrange(2,len(airports)//2)
    flights[airport] = [] #instead use flights.setdefault(airport,[])
    for d in range(numdestinations):
      newdest = r.choice(otherports)
      flights[airport].append(newdest)
      otherports.remove(newdest)
  return flights
      
def two_hops(routes,start,end):
  if end in routes[start]:
    return True
  else:
    for dest in routes[start]:
      if end in routes[dest]:
        return True
  return False
  
print("Example flights:---")
print(create_routes(airports))
print(" \n ")
print(two_hops(sample_routes,'LAX','SEA'))
print(two_hops(sample_routes,'JFK','SEA'))
start = r.choice(airports)
end = r.choice(airports)
print("From " + start + " to " + end + " :  " + str(two_hops(create_routes(airports),start,end)))