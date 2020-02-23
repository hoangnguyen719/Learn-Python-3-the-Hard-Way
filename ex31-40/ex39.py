states = {'Oregon': 'OR', 'Florida': 'FL', 'California': 'CA',
            'New York': 'NY', 'Michigan': 'MI'
            }

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York' # add new key-value pair to dict
cities['OR'] = 'Portland'

print('-' *10)
print('NY State has: ', cities['NY'])

print(*states.items(), sep = '\n')
print(*states.keys())
print(*states.values())
print(states.get('CA')) # this will print none
print(states.get('California')) #this will print value CA
