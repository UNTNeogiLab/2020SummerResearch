import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hyperspy as hs

class point:
    def __init__(self, x, y):
        self.intensity = []
        self.wave = []
        self.x = x
        self.y = y
    def add(self, intensity, wave):
        self.wave.append(wave)
        self.intensity.append(intensity)
    def graph(self):
        plt.plot(self.wave,self.intensity)
        plt.ylabel("intensity")
        plt.xlabel("wave")
        plt.title("Point:"+ str(self.x) + ","+ str(self.y))
        plt.show()
    def convert(self):
        self.data = hs.signals.Signal1D(np.array(self.intensity))

plt.close("all")
filename = "data/Sample1_map_data.txt"
raw = pd.read_csv(filename, delim_whitespace=True)
points = []
current_point = point(0,0)
used = False
for index,row in raw.iterrows():
    if row["#X"] == current_point.x and row["#Y"] == current_point.y :
        current_point.add(row["#Intensity"],row[ "#Wave"])
    else:
        points.append(current_point)
        current_point = point(row["#X"],row["#Y"])
        current_point.add(row["#Intensity"],row[ "#Wave"])
for point in points:
    point.graph()

