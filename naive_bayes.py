
def naive_bayes(dataset, main):
    probability = get_probability(dataset, main)
    main_probability = get_main_probability(dataset, main)

    import json
    print(json.dumps(main_probability, indent=1))
    print("")
    print(json.dumps(calculate_combined_probabilities(probability, main_probability), indent=1))

    temp = {'outlook': 'sunny',    'temperature': 'cool',   'humidity': 'high',     'windy': True}
    Px = 0

    for key, value in temp.items():
        x = get_main_probability(dataset, key)
        if Px== 0:
            Px = x[value]['count'] / len(dataset)
        else:
            Px *= x[value]['count'] / len(dataset)

    print(f"get Px: {Px}")
    print(f"YES should: {(2/9)*(3/9)*(3/9)*(3/9)*(9/14)}")
    print(f"NO should: {(3/5)*(1/5)*(4/5)*(3/5)*(5/14)}")
    print("{:.10f}".format(0.35714285714285715 * 0.00010532571428571432))
    # print(f"{get_main_probability(dataset, 'outlook')}")
                    

def calculate_combined_probabilities(data, main):
    probabilities = {}
    
    for feature_values in data.values():
        for values in feature_values.values():
            for outcome in values.keys():
                probabilities[outcome] = 0
    
    for keyX, feature_values in data.items():
        for keyY, values in feature_values.items():
            for outcome, stats in values.items():
                if stats['probability'] != 0:
                    print(f"\n{keyX} {keyY}\n {outcome} {probabilities[outcome]} *= {stats['probability']}")
                    if probabilities[outcome] == 0:
                        probabilities[outcome] = stats['probability']
                    else:
                        probabilities[outcome] *= stats['probability']

    for key, value in main.items():
            probabilities[key] *= main[key]['probability']

    return probabilities


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


def get_main_probability(dataset, main):
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
    
    return main_values


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

temp = [
    {'outlook': 'sunny',    'temperature': 'cool',   'humidity': 'high',     'windy': False}
]

naive_bayes(dataset, 'play')
