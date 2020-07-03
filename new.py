import ipywidgets as widgets
from utils.importer import *
from utils.func import *
import matplotlib.pyplot as plt
import hyperspy.api as hs
from panel.interact import interact, interactive, fixed, interact_manual
import panel as pn
import xarray as xr
import pandas as pd
import numpy as np
from renishawWiRE import WDFReader
import os
import hvplot
import time
import hvplot.xarray
import holoviews as hv
hv.extension('bokeh')
hs.preferences.GUIs.warn_if_guis_are_missing = False
plt.max_open_warning = False
hs.preferences.save()
#hs.preferences.gui()
print("Imported Packages")
#ds = xr.open_dataset('data/BigData.nc')
def plot(filename, wavelength = 1,Orientation=1,Polarization =1 ):
    extension = filename.split('.')[1]
    if(extension == "3nc"):

        ds = xr.open_dataset(filename, chunks = {'wavelength':wavelength})
        def plot2(wavelength):
            return hv.HeatMap(ds.isel(wavelength=wavelength))
        dmap = hv.DynamicMap(plot2, kdims = ['wavelength'])
        dmap.select(wavelength = 514)
        return pn.panel(dmap.redim.values(wavelength=range(1, 1022)))
    elif(extension == "5nc"):
        ds = xr.open_dataset(filename, chunks = {'wavelength':wavelength,'Orientation':Orientation,'Polarization':Polarization})
        def plot(wavelength, Orientation,Polarization):
            return hv.HeatMap(hv.HeatMap(ds.isel(wavelength=wavelength,Orientation = Orientation,Polarization= Polarization)))
        dmap = hv.DynamicMap(plot, kdims = ['wavelength','Orientation','Polarization'])
        return pn.panel(dmap.redim.values(wavelength=range(0, 5),Orientation = range(0,2),Polarization=range(0,180)))
    else:
        return "<br>\n#INVALID FILE TYPE"

def plot2(filename, wavelength, orientation=1, polarization=100):
    return plot("converted/" + filename, wavelength, orientation, polarization)


def generateplot(filename):
    extension = filename.split('.')[1]
    h2 = pn.pane.Markdown('''## Choose chunk size
    ''')
    h3 = pn.pane.Markdown('''
    ## Plot
    ''')
    if (extension == "3nc"):
        layout = pn.interact(plot2, filename=fixed(filename), wavelength=(1, 200), orientation=fixed(2),
                             polarization=fixed(200))
    if (extension == "5nc"):
        layout = pn.interact(plot2, filename=fixed(filename), wavelength=(1, 5), orientation=(1, 2),
                             polarization=(1, 200))
    return pn.Row(pn.Column(h2, layout[0]), pn.Column(h3, layout[1]))


h1 = pn.pane.Markdown('''
#Multidimensional spectral data visualizer
##Choose a file below
''')
layout = pn.interact(generateplot, filename=(os.listdir('converted')))
GUI = pn.Row(pn.Column(h1, layout[0]), layout[1])
GUI.show()
