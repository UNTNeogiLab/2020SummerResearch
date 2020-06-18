#!/usr/bin/env python 
# ============================
# 2020-06-17 
# 15:59 
# ============================
get_ipython().run_line_magic('matplotlib', '')
import pandas as pd
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
get_ipython().run_line_magic('matplotlib', '')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', '')
import pandas as pd
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
get_ipython().run_line_magic('matplotlib', '')
import pandas as pd
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
data= hs.signals.Signal1D(raw)
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
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
get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
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
data= hs.signals.Signal1D(raw)
data.axes_manager.gui()
data.axes_manager.gui_navigation_sliders()
data.plot()
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
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
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
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

get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs
hs.preferences.gui(toolkit="ipywidgets")
print("Imported Packages")
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
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
get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
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
get_ipython().run_line_magic('matplotlib', 'qt')
import pandas as pd
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
get_ipython().run_line_magic('matplotlib', 'qt')
import pandas as pd
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

