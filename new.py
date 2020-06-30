import ipywidgets as widgets
from utils.importer import *
from utils.func import *
import matplotlib.pyplot as plt
import hyperspy.api as hs
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
reader = WDFReader('data/Sample1_map_data.wdf')
reader.spectra = np.flip(reader.spectra,axis=2)
w = range(0,reader.spectra.shape[2])
x = range(0,reader.spectra.shape[0])
y = range(0,reader.spectra.shape[1])
data = xr.DataArray(reader.spectra,dims = ('x','y',"wavelength"), name = (reader.title),coords = {'x': x,'y': y,'wavelength': w})
ds= data.to_dataset()
ds.to_netcdf('data/NewData2.nc')
def plot(wavelength):
    return hv.HeatMap(ds.isel(wavelength=wavelength))
dmap = hv.DynamicMap(plot, kdims = ['wavelength'])
dmap.select(wavelength = 514)
hv_layout = pn.panel(dmap.redim.values(wavelength=range(1, 1022)))
server = hv_layout.show()
