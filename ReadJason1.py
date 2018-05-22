
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.basemap 
from mpl_toolkits.basemap import Basemap
import datetime
import matplotlib.colors
Data=Dataset('CorSSH_J1_C0006_P0240_20020315_025847_20020315_035459.nc','r')
Data=Dataset('CorSSH_J1_C0002_P0204_20020202_012102_20020202_021708.nc','r')
Data=Dataset('CorSSH_J1_C0001_P0204_20020123_032226_20020123_041838.nc','r')




print Data.variables
print Data.variables.keys()

lat= np.array(Data.variables['lat'][:])
lon= np.array(Data.variables['lon'][:])
altura= np.array(Data.variables['swh'][:])
time= np.array(Data.variables['time'][:]).astype(np.float)


fecha = np.array([datetime.datetime(2000,01,01)+\
datetime.timedelta(seconds = time[i]) for i in range(len(time))])



milat=np.where((lat>10) & (lat <15))
lati=lat[milat]

milon=np.where((lon>275) & (lon <285))
longi=lon[milon]













plt.figure()

m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \
  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
  resolution='c')

x, y = m(lon,lat)

cs = m.pcolormesh(x,y,Data,shading='flat',cmap=plt.cm.jet)

m.drawcoastlines()
m.fillcontinents()
m.drawmapboundary()
m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])


plt.colorbar(cs,orientation='vertical')
plt.title('Example 2: NWW3 Significant Wave Height from GRiB')
plt.show()


