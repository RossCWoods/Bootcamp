meals = [ 'yoghurt' , 'roll' , 'steak' ]
meals = ('Yoghurt', 'roll', 'steak ')
my_first_empty_dictionary = {}
my_second_empty_dictionary = dict()

meals = {'Breakfast' : 'Yoghurt', 'Lunch' : 'Roll', 'Dinner': 'Steak'}
print(meals)

silly_thing = { 1 : '2', 2 : '3', 4 : False }
print(silly_thing)

print(meals['Breakfast'])

# print(meals['Supper'])

print('Breakfast' in meals)

print('Supper' in meals)

meals['Supper'] = 'Pancakes'
print(meals)

meals['Dinner'] = 'Pasta'
print(meals)

del(meals['Breakfast'])
print(meals)

pocketMoney = {'John' : 5, 'Kelsie' : 10, 'Ross' : 15}
print(pocketMoney)

pocketMoney['Vlada'] = 20
print(pocketMoney)

print(list(meals))
print(meals.keys())

print(meals.values())

countries = {
    'UK': 'London',
    'Germany': 'Berlin'
}

print(countries)

countries = {
    'UK': {
        'Capital' : 'London',
        'Population' : 1000
    },
    'Germany': {
        'Capital' : 'Berlin',
        'Population' : 5
    }
}

print(countries)

germany_population = countries["Germany"] ['Population']
print(germany_population)

avengers = {
    'Iron Man': {
        'Name' : 'Tony Stark',
        'Moves' : {
            'Punch' : 10,
            'Kick' : 100
        }
    },
    'Hulk': {
        'Name' : 'Bruce Banner',
        'Moves' : {
            'Smash' : 1000,
            'Roll' : 500
        }
    }
}

print(avengers['Hulk']['Moves']['Smash'])