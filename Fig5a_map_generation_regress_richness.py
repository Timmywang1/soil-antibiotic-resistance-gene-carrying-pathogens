#!/bin/python
import gdal
import numpy as np
import sys
import pandas as pd


data = np.genfromtxt('regress_richness1.csv', delimiter = ',', filling_values=np.nan)


file1=gdal.Open('New_wc2.1_30s_bio_1.tif')
band1=file1.GetRasterBand(1)
mat=band1.ReadAsArray()
file1=gdal.Open('New_wc2.1_30s_bio_12.tif')
band1=file1.GetRasterBand(1)
map=band1.ReadAsArray()
file1=gdal.Open('New_wc2.1_30s_bio_14.tif')
band1=file1.GetRasterBand(1)
dp=band1.ReadAsArray()
file1=gdal.Open('New_Average_phh2o2.tif')
band1=file1.GetRasterBand(1)
ph=band1.ReadAsArray()
file1=gdal.Open('New_Average_clay2.tif')
band1=file1.GetRasterBand(1)
clay=band1.ReadAsArray()
file1=gdal.Open('New_Average_cfvo2.tif')
band1=file1.GetRasterBand(1)
cfv=band1.ReadAsArray()
file1=gdal.Open('New_Average_soc2.tif')
band1=file1.GetRasterBand(1)
soc=band1.ReadAsArray()
file1=gdal.Open('New_bio21.tif')
band1=file1.GetRasterBand(1)
rad=band1.ReadAsArray()
file1=gdal.Open('New_Contrast_01_05_1km_uint32.tif')
band1=file1.GetRasterBand(1)
brdf=band1.ReadAsArray()
file1=gdal.Open('New_Nadir_Reflectance_1.tif')
band1=file1.GetRasterBand(1)
ref=band1.ReadAsArray()



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

file1=gdal.Open('New_TotalNumber_Bootstrap_CoefVar.tif')
band1=file1.GetRasterBand(1)
maskocean=band1.ReadAsArray()
maskocean[np.isnan(maskocean)] = maskocean[1,1]
maskocean[maskocean==maskocean[1,1]]=0
maskocean[maskocean!=0]=1


mask=mat*map*dp*ph*clay*cfv*soc*rad*brdf*ref*maskocean

data_mask=data*mask



path1='New_Average_nitrogen2.tif'
output_path='AP_regress_richness1.tif'
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