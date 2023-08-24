# counter = 0
# my_number = 5

# while (counter < my_number):
#     print(f'counter is {counter}')
#     counter += 1

#     numbers = [1, 2, 3, 4, 5]

#     for number in numbers:
#         print(number * 3)


# total = 0 

# for number in numbers:
#     total = total + number
#     print (total)

# chickens = ['Margaret', 'Hetty', 'Henrietta', 'Audrey', 'Mabel']
# for chicken in chickens:
#     print(chicken)

chickens = [
     {'name' : 'Margaret', 'Age' : 2, 'Eggs' : 0},
     {'name' : 'Hetty', 'Age' : 1, 'Eggs' : 2},
     {'name' : 'Henrietta', 'Age' : 3, 'Eggs' : 1},
     {'name' : 'Audrey', 'Age' : 2, 'Eggs' : 0},
     {'name' : 'Mabel', 'Age' : 5, 'Eggs' : 1}]

for chicken in chickens:
    print(f'{chicken["name"]} is {chicken["Age"]}')

# total_eggs = 0

# for chicken in chickens:
#     total_eggs += chicken['Eggs']
#     chicken['Eggs'] = 0

# print(f'{total_eggs} eggs collected')
# print(chickens)

for chicken in chickens:
    if chicken['Eggs'] > 0:
        print('Woo Eggs!!!')