# Script to process ozone data to make CMIP6 forcing ancillary file.

import numpy as np
import iris

iris.FUTURE.netcdf_no_unlimited=True

all_data_jan=iris.load_cube('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*jan*.pp')
#all_data_feb=iris.load_cube('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*feb*.pp')
#all_data_mar=iris.load_cube('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*mar*.pp')
#all_data_apr=iris.load_cube('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*apr*.pp')
#all_data_may=iris.load_cube('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*may*.pp')
#all_data_jun=iris.load_cube('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*jun*.pp')
#all_data_jul=iris.load_cube('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*jul*.pp')
#all_data_aug=iris.load_cube('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*aug*.pp')
#all_data_sep=iris.load_cube('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*sep*.pp')
#all_data_oct=iris.load_cube('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*oct*.pp')
#all_data_nov=iris.load_cube('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*nov*.pp')
#all_data_dec=iris.load_cube('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*dec*.pp')

time_mean_jan=all_data_jan.collapsed('time',iris.analysis.MEAN)
#time_mean_feb=all_data_feb.collapsed('time',iris.analysis.MEAN)
#time_mean_mar=all_data_mar.collapsed('time',iris.analysis.MEAN)
#time_mean_apr=all_data_apr.collapsed('time',iris.analysis.MEAN)
#time_mean_may=all_data_may.collapsed('time',iris.analysis.MEAN)
#time_mean_jun=all_data_jun.collapsed('time',iris.analysis.MEAN)
#time_mean_jul=all_data_jul.collapsed('time',iris.analysis.MEAN)
#time_mean_aug=all_data_aug.collapsed('time',iris.analysis.MEAN)
#time_mean_sep=all_data_sep.collapsed('time',iris.analysis.MEAN)
#time_mean_oct=all_data_oct.collapsed('time',iris.analysis.MEAN)
#time_mean_nov=all_data_nov.collapsed('time',iris.analysis.MEAN)
#time_mean_dec=all_data_dec.collapsed('time',iris.analysis.MEAN)

iris.save(time_mean_jan,'/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/NIWA-processed/anwwa_time_mean_jan.nc')
#iris.save(time_mean_feb,'/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/NIWA-processed/anwwa_time_mean_feb.pp')
#iris.save(time_mean_mar,'/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/NIWA-processed/anwwa_time_mean_mar.pp')
#iris.save(time_mean_apr,'/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/NIWA-processed/anwwa_time_mean_apr.pp')
#iris.save(time_mean_may,'/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/NIWA-processed/anwwa_time_mean_may.pp')
#iris.save(time_mean_jun,'/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/NIWA-processed/anwwa_time_mean_jun.pp')
#iris.save(time_mean_jul,'/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/NIWA-processed/anwwa_time_mean_jul.pp')
#iris.save(time_mean_aug,'/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/NIWA-processed/anwwa_time_mean_aug.pp')
#iris.save(time_mean_sep,'/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/NIWA-processed/anwwa_time_mean_sep.pp')
#iris.save(time_mean_oct,'/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/NIWA-processed/anwwa_time_mean_oct.pp')
#iris.save(time_mean_nov,'/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/NIWA-processed/anwwa_time_mean_nov.pp')
#iris.save(time_mean_dec,'/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/NIWA-processed/anwwa_time_mean_dec.pp')



