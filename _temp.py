def calculate_combined_probabilities(data):
    probabilities = {}
    
    for feature_values in data.values():
        for values in feature_values.values():
            for outcome in values.keys():
                probabilities[outcome] = 0
    
    for feature_values in data.values():
        for values in feature_values.values():
            for outcome, stats in values.items():
                if stats['probability'] != 0:
                    if probabilities[outcome] == 0:
                        probabilities[outcome] = stats['probability']
                    else:
                        probabilities[outcome] *= stats['probability']


    for key, value in probabilities.items():
        probabilities[key] = "{:.10f}".format(value)


    return probabilities

data = {
 "outlook": {
  "sunny": {
   "yes": {
    "count": 2,
    "probability": 0.2222222222222222
   },
   "no": {
    "count": 3,
    "probability": 0.6
   }
  },
  "overcast": {
   "yes": {
    "count": 4,
    "probability": 0.4444444444444444
   },
   "no": {
    "count": 0,
    "probability": 0.0
   }
  },
  "rainy": {
   "yes": {
    "count": 3,
    "probability": 0.3333333333333333
   },
   "no": {
    "count": 2,
    "probability": 0.4
   }
  }
 },
 "temperature": {
  "cool": {
   "yes": {
    "count": 3,
    "probability": 0.3333333333333333
   },
   "no": {
    "count": 1,
    "probability": 0.2
   }
  },
  "hot": {
   "yes": {
    "count": 2,
    "probability": 0.2222222222222222
   },
   "no": {
    "count": 2,
    "probability": 0.4
   }
  },
  "mid": {
   "yes": {
    "count": 4,
    "probability": 0.4444444444444444
   },
   "no": {
    "count": 2,
    "probability": 0.4
   }
  }
 },
 "humidity": {
  "normal": {
   "yes": {
    "count": 6,
    "probability": 0.6666666666666666
   },
   "no": {
    "count": 1,
    "probability": 0.2
   }
  },
  "high": {
   "yes": {
    "count": 3,
    "probability": 0.3333333333333333
   },
   "no": {
    "count": 4,
    "probability": 0.8
   }
  }
 },
 "windy": {
  "false": {
   "yes": {
    "count": 6,
    "probability": 0.6666666666666666
   },
   "no": {
    "count": 2,
    "probability": 0.4
   }
  },
  "true": {
   "yes": {
    "count": 3,
    "probability": 0.3333333333333333
   },
   "no": {
    "count": 3,
    "probability": 0.6
   }
  }
 }
}

combined_probabilities = calculate_combined_probabilities(data)
print(combined_probabilities)