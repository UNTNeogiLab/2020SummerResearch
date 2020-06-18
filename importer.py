import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs


def read(filename):
    loadables = [
        "spd",
        "spc"
    ] #TODO fix list
    extension = filename.split('.', 1)[1]
    print(extension)
    if (extension == "txt"):
        raw = np.genfromtxt(filename, delimiter="\t", skip_header=1, usecols=(0, 1, 3), dtype=float)
        xCoords = np.unique(raw[:, [0]]).__len__()
        yCoords = np.unique(raw[:, [1]]).__len__()
        wavesize = int(raw.shape[0] / xCoords / yCoords)
        raw = (raw[:, [2]].reshape((xCoords, yCoords, wavesize)))
        return hs.signals.Signal1D(raw)
    if (extension in loadables):
        #TODO fix importing
        return hs.load(filename)
    else:
        print("INVALID FILE TYPE")
