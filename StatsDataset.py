import numpy as np
import statistics as stats


class OmniStatsClass:
    def __init__(self,data):
        self.data = np.array(data)

    def update_data(self,new_data):
        self.data = np.array(new_data)
        print("Data updated succesfully.")

    def get_mean(self):
        return np.mean(self.data)
    
    def get_median(self):
        return np.median(self.data)
    
    #since numpy does not have a designated mode function like mean and median
    def get_mode(self):
        try:
            return  stats.mode(self.data)
        except stats.StatisticsError:
            return f"{self.data} No Unique mode found"
    
    def get_std(self):
        return np.std(self.data)

    def get_var(self):
        return np.var(self.data)