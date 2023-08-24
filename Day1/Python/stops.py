stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

stops.append('Edinburgh Waverly')

stops.insert(0, 'Glasgow Queen St')

stops.insert(4, 'Polmont')
    
linlithgow = stops.index('Linlithgow')
print(linlithgow)

stops.remove('Livingston')

stops.pop(2)

numberofstops = len(stops)
print(numberofstops)

# sortedlist = sorted(stops)
# print (sortedlist)

stops.reverse()
print(stops)

for stop in stops:
    print(stop)