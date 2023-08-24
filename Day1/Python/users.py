users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

print(users["Jonathan"]['twitter'])

print(users["Erik"]['home_town'])

print(users["Erik"]['lottery_numbers'])

print(users["Avril"]['pets'][0]['species'])

eriklow = sorted(users['Erik']['lottery_numbers'])[0]
print(eriklow)

users["Erik"]['lottery_numbers'].append(7)
print(users["Erik"]['lottery_numbers'])

users["Erik"]['home_town'] = 'Edinburgh'
print(users['Erik']['home_town'])

users['Kelsie'] = {
    'twitter': 'kelmur',
    'lottery_numbers': [69, 69, 69, 69, 69],
    'home_town': 'Essex',
    'pets': [
        {
            'name': 'Mason',
            'species': 'Dog'
        }
    ]
}

print(users)