from Markov import Markov
import numpy as np
import pandas as pd
from collections import Counter

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

array = np.array(pd.read_csv("weather.csv", header = None))

max_freq = []
print('Number of occurrences of each weather condition over the 100 trials:')
for key in city_weather.keys():
    value = city_weather[key]
    m = Markov(day_zero_weather = value)
    m.load_data(array)
    predict_list = m.get_weather_for_day(7)
    count = Counter(predict_list)
    d = dict(count.items())
    print(key,':', d)
    max_freq.append(count.most_common(1))

print()
print('Most likely weather in seven days')
print('---------------------------------')

for i in range(7):
    print(list(city_weather.keys())[i],':', max_freq[i][0][0])
