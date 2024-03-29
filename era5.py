import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels-preliminary-back-extension',
    {
        'product_type': 'reanalysis',
        'variable': 'mean_sea_level_pressure',
        'year': '1968',
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': [
            '00:00', '06:00', '12:00',
            '18:00',
        ],
        'format': 'netcdf',
    },
    'download.nc')
