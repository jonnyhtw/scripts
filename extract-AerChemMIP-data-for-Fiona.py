
# coding: utf-8

# # Jupyter notebook to extract specific STASH codes and years from UM data

# In[1]:


import iris
import copy


# In[2]:


stash_list =['m01s01i207','m01s01i208','m01s01i209','m01s02i205','m01s02i206']
stash_constraint = [iris.AttributeConstraint(STASH=stash) for stash in stash_list]


# In[3]:


startyear = 1865
endyear   = 1894


# In[4]:


years = iris.Constraint(time=lambda cell: startyear <= cell.point.year <= endyear)


# In[5]:


suite1 = 'u-bi639'
suite2 = 'u-bi883'


# In[6]:


suite = copy.copy(suite1)


# In[7]:


user = 'zengg'


# In[8]:


directory = '/nesi/nobackup/niwa00003/'+user+'/cylc-run/'+suite+'/share/data/History_Data/'


# In[9]:


#cubes = iris.load(directory+'*py*', stash_constraint)


# In[10]:


#for i in range(len(cubes)):
#    print cubes[i].cell_methods


# In[11]:


#cubes_1_hour_interval = [cubes[i] for i in (0, 1, 3, 5, 6)]

#for i in range(len(cubes_1_hour_interval)):
#    print cubes_1_hour_interval[i].cell_methods


# In[12]:


outfile = './'+suite+'-'+str(startyear)+'-'+str(endyear)+'-annual-mean-01207-01208-01209-02205-02206.pp'

outdir = '/nesi/project/niwa00013/williamsjh/CMIP6/data-for-fiona/'


# In[13]:



#if os.path.exists(outfile):
#    os.remove(outfile)

#for i in range(len(cubes_1_hour_interval)):
#    iris.save(cubes_1_hour_interval[i].extract(years),outdir+outfile,append=True)


# In[15]:


def one_hour_interval_selector(cube):
    try:
        return "1 hour" in cube.cell_methods[0].intervals
        # or return cube.cell_methods[0].intervals == ("1 hour" )
    except IndexError:
        # if there are cubes without cell_methods
        return False


for i in range(len(stash_constraint)):
    print('i = ',i)
    cubes_1_hour_interval = iris.load(directory + '*py*', stash_constraint[i] &
                                      iris.Constraint(cube_func=one_hour_interval_selector))
    if i == 0:
        all_cubes = copy.copy(cubes_1_hour_interval)
    else:
        all_cubes.append(cubes_1_hour_interval)





# In[21]:


for i in range(len(cubes_1_hour_interval)):
    iris.save(cubes_1_hour_interval[i].extract(years),outdir+'foo.pp',append=True)

