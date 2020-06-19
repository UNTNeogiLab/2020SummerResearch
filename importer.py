import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs
from PIL import Image
from renishawWiRE import WDFReader
import os

def read(filename):
    loadables = pd.read_csv("config/import_config.csv")
    extension = filename.split('.', 1)[1]
    print(extension)
    if (extension == "jpg"):

        im = Image.open(filename)
        im.save("temp.png")
        data =  hs.load("temp.png")
        os.remove("temp.png")
        return data
    if (extension == "txt"):
        raw = np.genfromtxt(filename, delimiter="\t", skip_header=1, usecols=(0, 1, 3), dtype=float)
        xCoords = np.unique(raw[:, [0]]).__len__()
        yCoords = np.unique(raw[:, [1]]).__len__()
        wavesize = int(raw.shape[0] / xCoords / yCoords)
        raw = (raw[:, [2]].reshape((xCoords, yCoords, wavesize)))
        return hs.signals.Signal1D(raw)
    if (extension in loadables["extension"]):
        if(loadables["extension" == extension]["signal"] == ""):
            return hs.load(filename, signal_type=loadables["extension" == extension]["signal"])
        else:
            return hs.load(filename)
    if (extension == "wdf"):
        reader = WDFReader(filename)
        reader.print_info()
        return hs.signals.Signal1D(reader.spectra)
    else:
        print("INVALID FILE TYPE")
