import matplotlib.pyplot as plt
import numpy as np
import glob
from tqdm.notebook import tqdm
from rich.jupyter import print
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from rich.__main__ import make_test_card
import scipy
import airportsdata
import matplotlib.transforms as transforms
import cartopy.io.img_tiles as cimgt
from IPython.display import clear_output
import emoji
from scipy import interpolate
import math
import netCDF4 as nc
import string
from scipy import stats
from numpy import asarray
import cartopy.feature as cfeature
from matplotlib.patches import ConnectionPatch
import seaborn as sns
import pickle
from numpy import savetxt
import os
import numpy.ma as ma
import pandas as pd
import csv
import xarray as xr
from matplotlib.ticker import FormatStrFormatter
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from matplotlib.ticker import EngFormatter, StrMethodFormatter
from tqdm import tqdm
import numpy as np
import cartopy.crs as ccrs
import matplotlib.dates as mdates
from tqdm import tqdm
import datetime as dt
import nc_time_axis
import sys
from joblib import Parallel, delayed
from geopy.geocoders import Nominatim

