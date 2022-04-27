# NOTE TO SELF: RUN WITH CONDA

#notes: removed ufo sightings with durations longer than 5 hours and shorter than 5 seconds. 


from math import log

def csv_to_dict(file): # read csv into dictionary
    durs, lats, longs, commas = [],[],[],0
    for line in open(file):
        commas = 0
        dur, lat, lon = "", "", ""
        if line[0] !="d":
            for c in line:
                if c == ",":
                    commas += 1
                elif commas == 5:
                    dur += c
                elif commas == 9:
                    lat += c
                elif commas == 10:
                    lon += c
            lat, lon, dur = float(lat), float(lon), log(float(dur))
            if -125 < lon < -67 and 25 < lat < 49: # filter by contguous US latitude/longitude
                durs.append(dur)
                lats.append(lat)
                longs.append(lon)
    return {"log(duration)":durs, "latitudes": lats, "longitudes": longs}

import pandas
import seaborn
import matplotlib.pyplot as plt

df = pandas.DataFrame.from_dict(csv_to_dict("ufos.csv.csv")) # dictonary to dataframe

plt.rcParams['figure.figsize'] = [20, 10]
plt.rcParams['figure.dpi'] = 100
plt.rcParams['axes.facecolor'] = 'xkcd:grey'
plt.rcParams['figure.facecolor'] = 'xkcd:grey'
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = True, 
                bottom=False, top = False, left = False, labeltop=False)
plt.style.use("seaborn-dark")

p = seaborn.scatterplot(x = "longitudes", y = "latitudes", hue = "log(duration)", data = df, palette="rocket", size = "log(duration)", alpha = 0.75)
p.get_figure().savefig("test_us15.png",bbox_inches='tight',transparent=False)