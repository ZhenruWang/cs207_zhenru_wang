from Markov import Markov
import numpy as np
import pandas as pd

weather = np.array(pd.read_csv("weather.csv", header = None))
weather_today = Markov()
weather_today.load_data(weather)    # Where weather is a 2D array read in from a .csv file
#print(weather_today.get_prob('windy', 'cloudy'))
print(weather_today.get_prob('cloudy','windy'))
