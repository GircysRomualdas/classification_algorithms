
def naive_bayes(dataset, main):
    x = get_probability(dataset, main)
    y = get_main(dataset, 'play')


def count_occurrences(dataset, look, main):
    possible_values = set()
    
    for data in dataset:
        possible_values.add(data[main])
    
    counts = {key: {values: 0 for values in possible_values} for key in set(data[look] for data in dataset)}
    
    for data in dataset:
        key = data[look]
        outcome = data[main]
        counts[key][outcome] += 1
    
    return counts


def get_probability(dataset, main):
    total = len(dataset)
    main_occurrences = count_occurrences(dataset, main, main)
    columns = list(dataset[0].keys())
    columns.remove(main)
    probability = {}

    for column in columns:
        probability[column] = {}
        for keyX, valueX in count_occurrences(dataset, column, main).items(): 
            probability[column][keyX] = {}
            for keyY, valueY in main_occurrences.items():
                probability[column][keyX][keyY] = {
                    'count': valueX[keyY],
                    'probability': valueX[keyY] / valueY[keyY]
                }

    return probability


# fix leter get_main and get_probability look ? similar shorten one function and call another inside one and combine dictionaries ?
def get_main(dataset, main):
    main_values = {}
    total_count = len(dataset)
    main_counts = {}
    for data in dataset:
        value = data.get(main)
        if value in main_counts:
            main_counts[value] += 1
        else:
            main_counts[value] = 1
    
    for value, count in main_counts.items():
        probability = count / total_count
        main_values[value] = {'count': count, 'probability': probability}
    
    return {main: main_values}


dataset = [
    {'outlook': 'sunny',    'temperature': 'hot',   'humidity': 'high',     'windy': False, 'play': 'no'},
    {'outlook': 'sunny',    'temperature': 'hot',   'humidity': 'high',     'windy': True,  'play': 'no'},
    {'outlook': 'overcast', 'temperature': 'hot',   'humidity': 'high',     'windy': False, 'play': 'yes'},
    {'outlook': 'rainy',    'temperature': 'mid',   'humidity': 'high',     'windy': False, 'play': 'yes'},
    {'outlook': 'rainy',    'temperature': 'cool',  'humidity': 'normal',   'windy': False, 'play': 'yes'},
    {'outlook': 'rainy',    'temperature': 'cool',  'humidity': 'normal',   'windy': True,  'play': 'no'},
    {'outlook': 'overcast', 'temperature': 'cool',  'humidity': 'normal',   'windy': True,  'play': 'yes'},
    {'outlook': 'sunny',    'temperature': 'mid',   'humidity': 'high',     'windy': False, 'play': 'no'},
    {'outlook': 'sunny',    'temperature': 'cool',  'humidity': 'normal',   'windy': False, 'play': 'yes'},
    {'outlook': 'rainy',    'temperature': 'mid',   'humidity': 'normal',   'windy': False, 'play': 'yes'},
    {'outlook': 'sunny',    'temperature': 'mid',   'humidity': 'normal',   'windy': True,  'play': 'yes'},
    {'outlook': 'overcast', 'temperature': 'mid',   'humidity': 'high',     'windy': True,  'play': 'yes'},
    {'outlook': 'overcast', 'temperature': 'hot',   'humidity': 'normal',   'windy': False, 'play': 'yes'},
    {'outlook': 'rainy',    'temperature': 'mid',   'humidity': 'high',     'windy': True,  'play': 'no'}
]

naive_bayes(dataset, 'play')
