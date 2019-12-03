import numpy as np
import pandas as pd

class Markov:
    def __init__(self, day_zero_weather = None):
        self.day_zero_weather = day_zero_weather
        self.weather_list = ['sunny', 'cloudy', 'rainy', 'snowy', 'windy', 'hailing']
        #self.weather_list = ['Dry','Humid','Sunny']
        self.data = []
        
    def load_data(self,array):
        self.data = array
        #self.data = np.array(pd.read_csv("weather.csv", header = None))
        #print(self.data)
        
    def get_prob(self,current_day_weather, next_day_weather): 
        try:
            cur_idx = self.weather_list.index(current_day_weather)
        except:
            raise Exception ('current_day_weather is not one of the 6 strings specified')
            
        try:
            next_idx = self.weather_list.index(next_day_weather)
        except:
            raise Exception ('next_day_weather is not one of the 6 strings specified')
           
#        res = 0
#        for i in range(len(self.weather_list)):
#            res += self.data[cur_idx,i] * self.data[i,next_idx]
#        return res
        return self.data[cur_idx,next_idx]

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            cur_idx = self.weather_list.index(self._current_day_weather)
        except:
            raise Exception ('current_day_weather is not one of the 6 strings specified')
            
        p_list = self.data[cur_idx,:]
        next_day_weather = np.random.choice(self.weather_list, p = p_list)
        self._current_day_weather = next_day_weather
        return next_day_weather
    
    def _simulate_weather_for_day(self,day):
        assert day >= 0
        for i in range(day):
            next_day_weather = self.__next__()
        return next_day_weather
        
    
    def get_weather_for_day(self, day, trials = 100):
        res = []
        for i in range(trials):
            self._current_day = 0
            self._current_day_weather = self.day_zero_weather
            res.append(self._simulate_weather_for_day(day))
        return res

