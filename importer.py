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
        data = hs.load("temp.png")
        os.remove("temp.png")
        return data
    if (extension == "txt"):
        raw = np.genfromtxt(filename, delimiter="\t", skip_header=1, dtype=float, names =("X","Y","Wavelength","Intensity") )
        xCoords = np.unique(raw["X"]).__len__()
        yCoords = np.unique(raw[["Y"]]).__len__()
        wavesize = int(np.shape(raw)[0]/xCoords/yCoords)
        print(raw)
        raw = np.sort(raw, axis=-1, order = ("X","Y","Wavelength"))
        raw = (raw["Intensity"].reshape((xCoords, yCoords, wavesize)))  
        print(raw)
        return hs.signals.Signal1D(raw)
    if (extension in loadables["extension"]):
        if (loadables["extension" == extension]["signal"] == ""):
            return hs.load(filename, signal_type=loadables["extension" == extension]["signal"])
        else:
            return hs.load(filename)
    if (extension == "wdf"):
        reader = WDFReader(filename)
        reader.print_info()
        return hs.signals.Signal1D(reader.spectra)
    else:
        print("INVALID FILE TYPE")
