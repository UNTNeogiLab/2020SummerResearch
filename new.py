import matplotlib.pyplot as plt
import hyperspy.api as hs
from panel.interact import interact, interactive, fixed, interact_manual
import panel as pn
import xarray as xr
import colorcet as cc
import os
import plotly.express as px
import numpy as np
import holoviews as hv
hv.extension('bokeh')
pn.extension()
hs.preferences.GUIs.warn_if_guis_are_missing = False
plt.max_open_warning = False
hs.preferences.save()
#hs.preferences.gui()
print("Imported Packages")
#ds = xr.open_dataset('data/BigData.nc')
def plot(filename, wavelength = 1):
    extension = filename.split('.')[1]
    if(extension == "3nc"):

        ds = xr.open_dataset(filename, chunks = {'wavelength':wavelength})
        def plot2(wavelength):
            return hv.HeatMap(ds.isel(wavelength=wavelength)).opts(cmap = 'Reds',width = 900,colorbar = True)
        dmap = hv.DynamicMap(plot2, kdims = ['wavelength'])
        return pn.panel(dmap.redim.values(wavelength=ds.coords['wavelength'].values))
    elif(extension == "5nc"):
        ds = xr.open_dataset(filename, chunks = {'x':1,'y':1,'Orientation':1})
        def plot(x,y, Orientation):
            return hv.Image(np.log(ds['truncated_data'].isel(Orientation=Orientation,x= x, y = y))).opts(cmap = 'Blues',invert_axes = True,width = 1800,colorbar = True)
        layout = pn.interact(plot,x=ds.coords['x'].values,Orientation = ds.coords['Orientation'].values,y=ds.coords['y'].values)
        return pn.Row(layout[0],layout[1])
    else:
        return "<br>\n#INVALID FILE TYPE"


def plot2(filename,wavelength):
    return plot("converted/"+filename, wavelength)
def generateplot(filename):
    extension = filename.split('.')[1]
    h2 = pn.pane.Markdown('''## Choose chunk size
    ''')
    h3 = pn.pane.Markdown('''
    ## Plot
    ''')
    if (extension == "3nc"):
        layout = pn.interact(plot2,filename=fixed(filename), wavelength = (1,200))
        return pn.Row(pn.Column(h2,layout[0]),pn.Column(h3,layout[1]))
    if (extension == "5nc"):
        layout =  pn.interact(plot2,filename= fixed(filename), wavelength= fixed(1))
        return pn.Row(pn.Column(h3,layout[1]))


h1 = pn.pane.Markdown('''
#Multidimensional spectral data visualizer
##Choose a file below
''')
layout = pn.interact(generateplot,filename=(os.listdir('converted')))
GUI = pn.Row(pn.Column(h1,layout[0]),layout[1])
GUI.show()
