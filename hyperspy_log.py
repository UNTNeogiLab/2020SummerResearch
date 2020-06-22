#!/usr/bin/env python
# ============================
# 2020-06-18
# 00:15
# ============================
get_ipython().run_line_magic('matplotlib', 'qt')
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")
plt.close("all")
filename = "data/Sample1_map_data.txt"
raw =np.genfromtxt(filename ,delimiter="\t", skip_header=1, usecols= (0,1,3),dtype= float)
xCoords = np.unique(raw[:,[0]]).__len__()
yCoords = np.unique(raw[:,[1]]).__len__()
wavesize = int(raw.shape[0]/xCoords/yCoords)
raw = (raw[:,[2]].reshape((xCoords,yCoords,wavesize)))
print("Imported Data")
data= hs.signals.Signal1D(raw)
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()
plt.close("all")
filename = "data/Sample1_map_data.txt"
raw =np.genfromtxt(filename ,delimiter="\t", skip_header=1, usecols= (0,1,3),dtype= float)
xCoords = np.unique(raw[:,[0]]).__len__()
yCoords = np.unique(raw[:,[1]]).__len__()
wavesize = int(raw.shape[0]/xCoords/yCoords)
raw = (raw[:,[2]].reshape((xCoords,yCoords,wavesize)))
print("Imported Data")

data= hs.signals.Signal1D(raw)
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

plt.close("all")
filename = "data/Sample1_map_data.txt"
raw =np.genfromtxt(filename ,delimiter="\t", skip_header=1, usecols= (0,1,3),dtype= float)
xCoords = np.unique(raw[:,[0]]).__len__()
yCoords = np.unique(raw[:,[1]]).__len__()
wavesize = int(raw.shape[0]/xCoords/yCoords)
raw = (raw[:,[2]].reshape((xCoords,yCoords,wavesize)))
print("Imported Data")
data= hs.signals.Signal1D(raw)
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()
get_ipython().run_line_magic('matplotlib', 'qt')
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


get_ipython().run_line_magic('matplotlib', 'qt')
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")
plt.close("all")
filename = "data/Sample1_map_data.txt"
raw =np.genfromtxt(filename ,delimiter="\t", skip_header=1, usecols= (0,1,3),dtype= float)
xCoords = np.unique(raw[:,[0]]).__len__()
yCoords = np.unique(raw[:,[1]]).__len__()
wavesize = int(raw.shape[0]/xCoords/yCoords)
raw = (raw[:,[2]].reshape((xCoords,yCoords,wavesize)))
print("Imported Data")
plt.close("all")
filename = "data/Sample1_map_data.txt"
raw =np.genfromtxt(filename ,delimiter="\t", skip_header=1, usecols= (0,1,3),dtype= float)
xCoords = np.unique(raw[:,[0]]).__len__()
yCoords = np.unique(raw[:,[1]]).__len__()
wavesize = int(raw.shape[0]/xCoords/yCoords)
raw = (raw[:,[2]].reshape((xCoords,yCoords,wavesize)))
print("Imported Data")

data= hs.signals.Signal1D(raw)
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

gui_fname()
get_ipython().run_line_magic('gui', 'qt')


def gui_fname(dir=None):
    """Select a file via a dialog and return the file name."""
    if dir is None: dir ='./'
    fname = QFileDialog.getOpenFileName(None, "Select data file...",
                dir, filter="All files (*);; SM Files (*.sm)")
    return fname[0]
gui_fname()
get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


plt.close("all")
filename = gui_fname()
raw =np.genfromtxt(filename ,delimiter="\t", skip_header=1, usecols= (0,1,3),dtype= float)
xCoords = np.unique(raw[:,[0]]).__len__()
yCoords = np.unique(raw[:,[1]]).__len__()
wavesize = int(raw.shape[0]/xCoords/yCoords)
raw = (raw[:,[2]].reshape((xCoords,yCoords,wavesize)))
print("Imported Data")

data= hs.signals.Signal1D(raw)
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


plt.close("all")
filename = gui_fname()
raw =np.genfromtxt(filename ,delimiter="\t", skip_header=1, usecols= (0,1,3),dtype= float)
xCoords = np.unique(raw[:,[0]]).__len__()
yCoords = np.unique(raw[:,[1]]).__len__()
wavesize = int(raw.shape[0]/xCoords/yCoords)
raw = (raw[:,[2]].reshape((xCoords,yCoords,wavesize)))
print("Imported Data")

data= hs.signals.Signal1D(raw)
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")
get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")
plt.close("all")
filename = gui_fname()
raw =np.genfromtxt(filename ,delimiter="\t", skip_header=1, usecols= (0,1,3),dtype= float)
xCoords = np.unique(raw[:,[0]]).__len__()
yCoords = np.unique(raw[:,[1]]).__len__()
wavesize = int(raw.shape[0]/xCoords/yCoords)
raw = (raw[:,[2]].reshape((xCoords,yCoords,wavesize)))
print("Imported Data")
plt.close("all")
filename = gui_fname()
raw =np.genfromtxt(filename ,delimiter="\t", skip_header=1, usecols= (0,1,3),dtype= float)
xCoords = np.unique(raw[:,[0]]).__len__()
yCoords = np.unique(raw[:,[1]]).__len__()
wavesize = int(raw.shape[0]/xCoords/yCoords)
raw = (raw[:,[2]].reshape((xCoords,yCoords,wavesize)))
print("Imported Data")
get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
import matplotlib.pyplot as plt
import hyperspy.api as hs
plt.close(all)
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
import matplotlib.pyplot as plt
import hyperspy.api as hs
plt.close(all)
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

data = read(gui_fname())

data = hs.load("data/MoS2_Map1_Copy.spc")
get_ipython().run_line_magic('pinfo', 'hs')


hs.load


hs.load()


get_ipython().run_line_magic('pinfo', 'hs.load')


data = hs.load("data/MoS2_Map1_Copy.spc",signal_type=EDSSEMSpectrum )
data = hs.load("data/MoS2_Map1_Copy.spc",signal_type="EDSSEMSpectrum")
data = hs.load("data/MoS2_Map1_Copy.spc",signal_type="EDSSEMSpectrum")
data = read(gui_fname())

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

data = hs.load("data/MoS2_Map1_Copy.spc",signal_type="EDSSEMSpectrum")
data = hs.load("data/RamanSpec.spc",signal_type="EDSSEMSpectrum")
data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

data = read(gui_fname())

data = read(gui_fname())

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

data = hs.load("data/RamanSpec.spc",signal_type="EDSSEMSpectrum")

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

data = read(gui_fname())

data = read(gui_fname())

data = read(gui_fname())

data = read(gui_fname())

data = read(gui_fname())

data = read(gui_fname())

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

data = hs.load("data/RamanSpec.spc",signal_type="EDSSEMSpectrum")

data = hs.load("data/RamanSpec.spc",signal_type="EDSSEMSpectrum")

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

data = hs.load("data/RamanSpec.spc",signal_type="EDSSEMSpectrum")

data = hs.load("data/RamanSpec.spc",signal_type="EDSSEMSpectrum")


np.version.version()
data = hs.load("data/RamanSpec.spc",signal_type="EDSSEMSpectrum")


np.version.version()
data = hs.load("data/RamanSpec.spc",signal_type="EDSSEMSpectrum")


np.version.version()
data = hs.load("data/RamanSpec.spc",signal_type="EDSSEMSpectrum")


np.version.version
data = hs.load("data/RamanSpec.spc",signal_type="EDSSEMSpectrum")


np.version
data = hs.load("data/RamanSpec.spc",signal_type="EDSSEMSpectrum")


np.version

np.version.version

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot(navigator="spectrum")

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot(navigator="spectrum")

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.find_peaks1D_ohaver()
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
print(data.find_peaks1D_ohaver())
data.plot()

data = read(gui_fname())
data = read(gui_fname())
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
print(data.find_peaks1D_ohaver())
data.plot()
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
print(data.find_peaks1D_ohaver())
data.plot()
get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'webagg')
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'webagg')
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'WebAgg')
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'WX')
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'WX')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

data = read(gui_fname())

data = read(gui_fname())

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
print(data.find_peaks1D_ohaver())
data.plot(colorbar=True)

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
print(data.find_peaks1D_ohaver())
data.plot(colorbar=True)

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
print(data.find_peaks1D_ohaver())
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
print(data.find_peaks1D_ohaver())
data.plot(navigator = "sliders")

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
print(data.find_peaks1D_ohaver())
data.plot(navigator = "slider")

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#print(data.find_peaks1D_ohaver())
data.plot(navigator = "slider")

data.metadata

data = read(gui_fname())

data.metadata

data.metadata

data.metadata

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#print(data.find_peaks1D_ohaver())
data.plot(navigator = "slider")

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#print(data.find_peaks1D_ohaver())
data.plot()

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#print(data.find_peaks1D_ohaver())
data.plot()

data = read(gui_fname())

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

data = read(gui_fname())

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

data = read(gui_fname())

data = read(gui_fname())

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#print(data.find_peaks1D_ohaver())
data.plot()

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#print(data.find_peaks1D_ohaver())
data.plot()

data = read(gui_fname())

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")


data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
#print(data.find_peaks1D_ohaver())
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
#print(data.find_peaks1D_ohaver())
data.plot()

data = read(gui_fname())
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
#print(data.find_peaks1D_ohaver())
data.plot()
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")
data = read(gui_fname())
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *

print("Imported Packages")
data = read(gui_fname())
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
#print(data.find_peaks1D_ohaver())
data.plot()
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
#print(data.find_peaks1D_ohaver())
data.plot()
get_ipython().run_line_magic('matplotlib', 'notebook')
from utils.func import *
from utils.importer import *

print("Imported Packages")
data = read(gui_fname())
data = read(gui_fname())
data = read(gui_fname())
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
#print(data.find_peaks1D_ohaver())
data.plot()
get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
import hyperspy.api as hs
hs.preferences()
print("Imported Packages")


get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences
print("Imported Packages")


data = read(gui_fname())

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")


data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
#print(data.find_peaks1D_ohaver())
data.plot()

data.transpose()
data.plot()

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")


data = read(gui_fname())

data.transpose()
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
#print(data.find_peaks1D_ohaver())
data.plot()

data.transpose()
data.plot(navigator= "slider")

data2 =  data.roi.SpanROI(200,400)

band =  hs.roi.SpanROI(200,400)
data2 = band(data)
data2.plot()
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
#print(data.find_peaks1D_ohaver())
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
#print(data.find_peaks1D_ohaver())
data.plot()

band =  hs.roi.SpanROI(200,400)
data2 = band(data)
data2.plot()
band =  hs.roi.SpanROI()
data2 = band(data)
data2.plot()
band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()
band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()
band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
#print(data.find_peaks1D_ohaver())
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
#print(data.find_peaks1D_ohaver())
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate(data.find_peaks1D_ohaver()[0:1])
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.calibrate()
print(data.find_peaks1D_ohaver())
data.plot()

data.transpose()
for image in data:
    image.plot()


data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data = read(gui_fname())

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.plot()

data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.calibrate()

data.plot()
data.plot()
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()

data.plot()
data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()

data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()

data.plot()
data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.calibrate()

data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.calibrate()

data.plot()
data = read(gui_fname())

#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.calibrate()

#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
print(data.find_peaks1D_ohaver())
data.calibrate()

#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()

data.plot()

#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")


data = read(gui_fname())

#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()

data.plot()

data.plot()

data = read(gui_fname())

data.plot()

data = read(gui_fname())

#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")


data = read(gui_fname())

data = read(gui_fname())

data = read(gui_fname())

data = read(gui_fname())

data = read(gui_fname())

data.plot()

data = read(gui_fname())

get_ipython().run_line_magic('gui', 'qt')
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")


data = read(gui_fname())

data = read(gui_fname())

#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()

data = read(gui_fname())
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
data.plot()
data = read(gui_fname())
get_ipython().run_line_magic('matplotlib', 'qt')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
data = read(gui_fname())
get_ipython().run_line_magic('matplotlib', 'notebook')
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'notebook')
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'notebook')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
data = read(gui_fname())
data = read(gui_fname())
my_button = SelectFilesButton()
my_button
data = read()
my_button = SelectFilesButton()
my_button
data = read()
get_ipython().run_line_magic('matplotlib', 'notebook')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
my_button = SelectFilesButton()
my_button
data = read()
my_button = SelectFilesButton()
my_button
data = read(my_button.file)
my_button = SelectFilesButton()
my_button
data = read(my_button.out)
my_button = SelectFilesButton()
my_button
data = read(my_button.files)
my_button = SelectFilesButton()
my_button
data = read(out)
data = read(gui_fname())
data = read(gui_fname().encode())
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
get_ipython().run_line_magic('matplotlib', 'notebook')
import hyperspy.api as hs
hs.preferences.GUIs.enable_traitsui_gui = False
hs.preferences.GUIs.enable_ipython_gui = True
hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'notebook')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.GUIs.enable_traitsui_gui = False
hs.preferences.GUIs.enable_ipython_gui = True
#hs.preferences.gui()
print("Imported Packages")
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
data.plot()
data = hs.load("data/RamanSpec.spc",signal_type="EDSSEMSpectrum")
get_ipython().run_line_magic('matplotlib', 'notebook')
import hyperspy.api as hs
hs.preferences.GUIs.enable_traitsui_gui = False
hs.preferences.GUIs.enable_ipython_gui = True
#hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.GUIs.enable_traitsui_gui = False
hs.preferences.GUIs.enable_ipython_gui = True
#hs.preferences.gui()
print("Imported Packages")
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
data.plot()
get_ipython().run_line_magic('matplotlib', 'widget')
import hyperspy.api as hs
hs.preferences.GUIs.enable_traitsui_gui = False
hs.preferences.GUIs.enable_ipython_gui = True
#hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')
import hyperspy.api as hs
hs.preferences.GUIs.enable_traitsui_gui = False
hs.preferences.GUIs.enable_ipython_gui = True
hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')
import hyperspy.api as hs
hs.preferences.GUIs.enable_traitsui_gui = False
hs.preferences.GUIs.enable_ipython_gui = True
hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')

import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')
import ipywidgets as widgets
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
data.plot()
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
data.plot()
out = widgets.Output(data.plot())
get_ipython().run_line_magic('matplotlib', 'widget')
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')
import ipywidgets as widgets
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
out = widgets.Output(data.plot())
get_ipython().run_line_magic('matplotlib', 'widget')
import ipywidgets as widgets
import hyperspy.api as hs
out= widgets.Output(hs.preferences.gui())
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')
import ipywidgets as widgets
import hyperspy.api as hs
out = widgets.Output(hs.preferences.gui()[0])
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')
import ipywidgets as widgets
import hyperspy.api as hs
out = widgets.Output(hs.preferences.gui()[1])
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'widget')
import ipywidgets as widgets
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
data = read(gui_fname().decode("utf-8"))
data = read(gui_fname().decode("utf-8"))
out = widgets.Output(data.plot())
data.plot()
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
data.plot()
data = read(gui_fname().decode("utf-8"))
data.plot()
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
data = read(gui_fname().decode("utf-8"))
get_ipython().run_line_magic('matplotlib', 'widget')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
data = read(gui_fname().decode("utf-8"))
data = read(gui_fname().decode("utf-8"))
data = read(gui_fname().decode("utf-8"))
data = read(gui_fname().decode("utf-8"))
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
data = read(gui_fname().decode("utf-8"))
data = read(gui_fname().decode("utf-8"))
data.plot()
get_ipython().run_line_magic('matplotlib', 'widget')
from utils.func import *
from utils.importer import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
data = read(gui_fname().decode("utf-8"))
data.plot()
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
data.plot()
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
data = read(gui_fname().decode("utf-8"))
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
data = read(gui_fname().decode("utf-8"))
#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()
get_ipython().run_line_magic('matplotlib', 'widget')
from utils.func import *
import hyperspy.api as hs
hs.preferences.gui()
print("Imported Packages")
data.plot()
data.plot()
data.plot()
data = read(gui_fname().decode("utf-8"))
data = read(gui_fname().decode("utf-8"))
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('ls', '/config')
get_ipython().run_line_magic('ls', './config')
get_ipython().system('ls ./config')
get_ipython().system('dir ./config')
get_ipython().system('dir .\\config')
data = read(gui_fname().decode("utf-8"))
data.plot()
band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()
data[3].plot()
data.plot()
data[isig].plot()
data.isig[3].plot()
def f(x):
    return x
interact(f, x=10);
data.isig[x].plot()
def f(x):
    return x
interact(f, x=10);
data.isig[x].plot()
data.isig[x.result].plot()
def f(x):
    return x
w= widgets.interactive(f, x=10);
x
data.isig[x].plot()
w
data.isig[x].plot()
w
data.isig[w].plot()
w
data.isig[w.result].plot()
w
data.isig[w.result]
w
data2 = data.isig[w.result]
data2.plot()
def f(x):
    return x
data2 = data.isig[w.
interact(f, x=10)]
data2 = data.isig[
interact(f, x=10)]
data2 = data.isig[int(interact(f, x=10))]
def f(x):
    return x
w = widgets.IntSlider()
display(w)
data2 = data.isig[int(w.output)].plot()
display(w)
data2 = data.isig[int(w.result)].plot()
def f(x):
    return x
w = widgets.interactive(f,a=10)
def f(x):
    return x
w = widgets.interactive(f,x=10)
display(w)
data2 = data.isig[int(w.result)].plot()
def f(x):
    return x
w = widgets.interactive(f,x=(0,1023))
display(w)
data2 = data.isig[int(w.result)].plot()
display(w)
data2 = data.isig[int(w.result)].plot()
display(w)
data2 = data.isig[int(w.result)].plot()
display(w)
data2 = data.isig[int(w.result)].plot()
display(w)
data2 = data.isig[int(w.result)].plot()
data2 = data.isig[int(w.result)].plot()
data2 = data.isig[int(w.result)].plot()
data2 = data.isig[int(w.result)].plot()
data = read(gui_fname().decode("utf-8"))
display(w)
data2 = data.isig[int(w.result)].plot()
data2 = data.isig[int(w.result)].plot()
data2 = data.isig[int(w.result)].plot()
def f(x):
    return x
w = widgets.interactive(f,x=(0,1023))

data = read(gui_fname().decode("utf-8"))

#data.axes_manager.gui()
#data.axes_manager.gui_navigation_sliders()
#data.crop_signal1D(200,400)
#print(data.find_peaks1D_ohaver())
data.calibrate()


display(w)

data2 = data.isig[int(w.result)].plot()

band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()

band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()

band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()

band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()

band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()

band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()

band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()

band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()

band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()

band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()

band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()

band =  hs.roi.SpanROI(1,2)
data2 = band(data)
data2.plot()

def f(x):
    return x
w = widgets.interactive(f,x=(0,1023))
data = read(gui_fname().decode("utf-8"))
display(w)
w = widgets.IntSlider()
display(w)
data2 = data.isig[int(w.result)].plot()
data2 = data.isig[int(w.value)].plot()
data2 = data.isig[int(w.value)].plot()
data2 = data.isig[int(w.value)].plot()
display(w)
w.value
display(w)
w.value
data2 = data.isig[int(w.value)].plot()
data2 = data.isig[int(w.value)].plot()
data2 = data.isig[int(w.value)].plot()
def on_change(change):
    if change['name'] == 'value' and (change['new'] != change['old']):
        clear_output()
        data.isig[int(w.value)].plot()
        sns.boxplot(data = mydata[change['new']])
display(w)
w.value
def on_change(change):
    if change['name'] == 'value' and (change['new'] != change['old']):
        clear_output()
        data.isig[int(w.value)].plot()
        sns.boxplot(data = mydata[change['new']])
display(w)
w.observe(on_change)
def on_change(change):
    if change['name'] == 'value' and (change['new'] != change['old']):
        clear_output()
        data.isig[int(w.value)].plot()
display(w)
w.observe(on_change)
def on_change(change):
    with output:
        data.isig[int(w.value)].plot()
display(w)
w.observe(on_change)
data.isig[int(w.value)].plot()
def on_change(change):
    with output:
        data.isig[int(w.value)].plot()
display(w)
w.observe(on_change, names = 'value')
with output:
        data.isig[int(w.value)].plot()
def on_change(change):
    with output:
        data.isig[int(w.value)].plot()
display(w)
w.observe(on_change, names = 'value')
def on_change(change):
    print ( "Hi")
    with output:
        data.isig[int(w.value)].plot()
display(w)
w.observe(on_change, names = 'value')
output = widgets.output()
def on_change(change):
    print ( "Hi")
    with output:
        data.isig[int(w.value)].plot()

w.observe(on_change, names = 'value')
display(w)
output = widgets.Output()
def on_change(change):
    print ( "Hi")
    with output:
        data.isig[int(w.value)].plot()

w.observe(on_change, names = 'value')
display(w)
output = widgets.Output()
def on_change(change):
    
    with output:
        print ( "Hi")

        data.isig[int(w.value)].plot()

w.observe(on_change, names = 'value')
display(w)
output = widgets.Output()
def on_change(change):
    with output:
        print ( "Hi")
        data.isig[int(w.value)].plot()

w.observe(on_change, names = 'value')
display(w, output)
output = widgets.Output()
def on_change(change):
    with output:
        print ( "Hi")
        plt.close("all")
        data.isig[int(w.value)].plot()

w.observe(on_change, names = 'value')
display(w, output)
output = widgets.Output()
def on_change(change):
    with output:
        print ( "Hi")
        plt.close('all')
        data.isig[int(w.value)].plot()

w.observe(on_change, names = 'value')
display(w, output)
data.isig[int(w.value)].plot()
plt.close('all')
data.isig[int(w.value)].plot()
plt.close('all')
plt.close('all')
data.isig[int(w.value)].plot()
plt.close('all')
data.plot(navigator='spectrum')
data.tranpose
data.plot(navigator='spectrum')
data.t
data.plot(navigator='spectrum')
data.T
data.plot(navigator='spectrum')
data.T
data.plot(navigator='spectrum')
data.spikes_removal_tool()
data.plot()
with output:
    data.plot()
