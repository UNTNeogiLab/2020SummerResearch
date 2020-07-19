import xarray as xr
import os
import numpy as np
def upgrade(filename):
    ds = xr.open_dataset(filename, chunks = {'Orientation':1,'x':10,'y':10})['5data']
    da1= np.log(ds)
    da2=  da1.mean(dim = ['Polarization'])
    da3=  ds.mean(dim = ['x','y'])
    ds2 = xr.Dataset({"da1":da1,"da2":da2,"da3":da3,"ds":ds},attrs=ds.attrs)
    ds2.to_netcdf(filename+'e', engine="h5netcdf")
dir = os.listdir('converted')
files = [file for file in dir if (file.split(".",1)[1] == "5nc" and (file.split(".",1)[0]+".5nce")not in dir )]
print(files)
for file in files:
    filename = "converted/"+file
    output = "converted/"+file.split(".",1)[0]
    upgrade(filename)
    print("upgraded: " + filename + " to " + output + ".5nce")
