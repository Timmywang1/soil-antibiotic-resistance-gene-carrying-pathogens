#!/bin/python
import gdal
import numpy as np
import sys
import pandas as pd


data = np.genfromtxt('AP_regress_richness2023.csv', delimiter = ',', filling_values=np.nan)


file1=gdal.Open('mat.tif')
band1=file1.GetRasterBand(1)
mat=band1.ReadAsArray()
file1=gdal.Open('map.tif')
band1=file1.GetRasterBand(1)
map=band1.ReadAsArray()
file1=gdal.Open('dp.tif')
band1=file1.GetRasterBand(1)
dp=band1.ReadAsArray()
file1=gdal.Open('ph.tif')
band1=file1.GetRasterBand(1)
ph=band1.ReadAsArray()
file1=gdal.Open('clay.tif')
band1=file1.GetRasterBand(1)
clay=band1.ReadAsArray()
file1=gdal.Open('cfv.tif')
band1=file1.GetRasterBand(1)
cfv=band1.ReadAsArray()
file1=gdal.Open('soc.tif')
band1=file1.GetRasterBand(1)
soc=band1.ReadAsArray()
file1=gdal.Open('rad.tif')
band1=file1.GetRasterBand(1)
rad=band1.ReadAsArray()
file1=gdal.Open('brdf.tif')
band1=file1.GetRasterBand(1)
brdf=band1.ReadAsArray()
file1=gdal.Open('ref.tif')
band1=file1.GetRasterBand(1)
ref=band1.ReadAsArray()
file1=gdal.Open('biomass.tif')
band1=file1.GetRasterBand(1)
biomass=band1.ReadAsArray()
file1=gdal.Open('northness.tif')
band1=file1.GetRasterBand(1)
northness=band1.ReadAsArray()
file1=gdal.Open('entropy.tif')
band1=file1.GetRasterBand(1)
entropy=band1.ReadAsArray()
file1=gdal.Open('evaporation.tif')
band1=file1.GetRasterBand(1)
evaporation=band1.ReadAsArray()
file1=gdal.Open('hdi.tif')
band1=file1.GetRasterBand(1)
hdi=band1.ReadAsArray()
file1=gdal.Open('pd.tif')
band1=file1.GetRasterBand(1)
pd=band1.ReadAsArray()


mat[1,1]
mat[mat==mat[1,1]]=0
mat[mat!=0]=1
map[1,1]
map[map==map[1,1]]=0
map[map!=0]=1
dp[1,1]
dp[dp==dp[1,1]]=0
dp[dp!=0]=1
ph[1,1]
ph[ph==ph[1,1]]=0
ph[ph!=0]=1
clay[1,1]
clay[clay==clay[1,1]]=0
clay[clay!=0]=1
cfv[1,1]
cfv[cfv==cfv[1,1]]=0
cfv[cfv!=0]=1
soc[1,1]
soc[soc==soc[1,1]]=0
soc[soc!=0]=1
rad[1,1]
rad[rad==rad[1,1]]=0
rad[rad!=0]=1
brdf[1,1]
brdf[brdf==brdf[1,1]]=0
brdf[brdf!=0]=1
ref[1,1]
ref[ref==ref[1,1]]=0
ref[ref!=0]=1
biomass[1,1]
biomass[biomass==biomass[1,1]]=0
biomass[biomass!=0]=1
northness[1,1]
northness[northness==northness[1,1]]=0
northness[northness!=0]=1
entropy[1,1]
entropy[entropy==entropy[1,1]]=0
entropy[entropy!=0]=1
evaporation[1,1]
evaporation[evaporation==evaporation[1,1]]=0
evaporation[evaporation!=0]=1
hdi[1,1]
hdi[hdi==hdi[1,1]]=0
hdi[hdi!=0]=1
pd[1,1]
pd[pd==pd[1,1]]=0
pd[pd!=0]=1

file1=gdal.Open('New_TotalNumber_Bootstrap_CoefVar.tif')
band1=file1.GetRasterBand(1)
maskocean=band1.ReadAsArray()
maskocean[np.invert(np.isnan(maskocean))]=1
maskocean[np.isnan(maskocean)]=0

mask=mat*map*dp*ph*clay*cfv*soc*rad*brdf*ref*biomass*northness*entropy*evaporation*hdi*pd*maskocean

data_mask=data*mask



path1='New_Average_nitrogen2.tif'
output_path='AP_regress_richness2023.tif'
driver=gdal.GetDriverByName('GTiff')
file1=gdal.Open(path1)
geotrans=file1.GetGeoTransform()
proj=file1.GetProjection()
band1=file1.GetRasterBand(1)
file2=driver.Create(output_path,band1.XSize,band1.YSize,1,band1.DataType)
file2.SetGeoTransform(geotrans)
file2.SetProjection(proj)
band2=file2.GetRasterBand(1)
Array_New=data_mask
band2.WriteArray(Array_New)
file2=None
