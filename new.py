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
        with xr.open_dataset(filename, chunks = {'wavelength':wavelength}) as ds:
            def plot2(wavelength):
                return hv.HeatMap(ds.isel(wavelength=wavelength)).opts(cmap = 'Reds',width = 900,colorbar = True)
            dmap = hv.DynamicMap(plot2, kdims = ['wavelength'])
            return pn.panel(dmap.redim.values(wavelength=ds.coords['wavelength'].values))
    elif(extension == "5nc"):
        with xr.open_dataset(filename, chunks = {'Orientation':1}) as ds:
            def plot(Orientation,Wavelength):
                polys = hv.Polygons([]).opts(fill_alpha=0.2, line_color='white')
                box_stream = hv.streams.BoxEdit(source=polys,num_objects = 1)
                def plot3(data, Orientation=Orientation):
                    if not data or not any(len(d) for d in data.values()):
                        output = np.log(ds.isel(Orientation=Orientation).mean(dim = ['x','y']))
                        return hv.Image(output).opts(cmap = 'Blues',invert_axes = True,width = 900,colorbar = True,title=(f" Orientation: {Orientation}"))
                    output = np.log(ds.isel(Orientation=Orientation,x=range(round(data['x0'][0]),round(data['x1'][0])),y = range(round(data['y0'][0]),round(data['y1'][0]))).mean(dim = ['x','y']))
                    return hv.Image(output).opts(cmap = 'Reds',invert_axes = True,width = 900,colorbar = True,title=(f"Orientation: {Orientation}"))
                def plot2(Orientation, wavelength):
                    return hv.HeatMap(ds.isel(Orientation=Orientation,wavelength = wavelength).mean(dim = 'Polarization')).opts(colorbar = True,title=(f"Wavelength: {wavelength}, Orientation: {Orientation}"))
                dmap = hv.DynamicMap(plot3, streams=[box_stream])
                return plot2(Orientation,Wavelength)*polys + dmap
        layout = pn.interact(plot, Orientation = ds.coords['Orientation'].values,Wavelength = ds.coords['wavelength'].values)
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
GUI.servable()
