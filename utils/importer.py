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
    if (extension == "jpg"):
        im = Image.open(filename)
        im.save("temp.png")
        data = hs.load("temp.png")
        os.remove("temp.png")
        return data
    '''
    if (extension == "txt"):
        raw = np.genfromtxt(filename, delimiter="\t", skip_header=1, dtype=float, names =("X","Y","Wavelength","Intensity"))
        #raw["X"] *= -1
        xCoords = np.unique(raw["X"]).__len__()
        yCoords = np.unique(raw["Y"]).__len__()
        wavesize = int(np.shape(raw)[0]/xCoords/yCoords)
        raw = np.sort(raw, axis=-1, order = ("Y","X","Wavelength"))
        raw = (raw["Intensity"].reshape((xCoords, yCoords, wavesize)))
        data = hs.signals.Signal1D(raw)
        data.metadata.General.title = filename.split('.',1)[0]
        data.axes_manager[0].name = 'x'
        data.axes_manager[1].name = 'y'
        data.axes_manager[2].name = 'wavelength'
        data.axes_manager[0].units = "um"
        data.axes_manager[1].units = "um"
        data.axes_manager[2].units = "1/cm"
        return data
    '''
    if (extension in loadables["extension"]):
        if (loadables["extension" == extension]["signal"] == ""):
            return hs.load(filename, signal_type=loadables["extension" == extension]["signal"])
        else:
            return hs.load(filename)
    if (extension == "wdf"):
        reader = WDFReader(filename)
        reader.spectra = np.flip(reader.spectra,axis=2)
        data = hs.signals.Signal1D(reader.spectra)
        data.metadata.General.title = reader.title
        data.metadata.General.authors = reader.username
        data.axes_manager[0].name = 'x'
        data.axes_manager[1].name = 'y'
        data.axes_manager[2].name = 'wavelength'
        data.axes_manager[0].units = str(reader.xpos_unit).replace('μ', 'u')
        data.axes_manager[1].units = str(reader.ypos_unit).replace('μ', 'u')
        data.axes_manager[2].units = str(reader.xlist_unit)
        return data
    else:
        print("INVALID FILE TYPE")
