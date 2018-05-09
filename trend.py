
# coding: utf-8

# In[16]:


from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('C:/Users/user/Desktop/pblc comp/EL-beauty.csv', header=4000)
series.plot()
pyplot.show()
print(series.shape)


# In[17]:


from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose
series = Series.from_csv('C:/Users/user/Desktop/pblc comp/EL-beauty.csv', header=4000)
result = seasonal_decompose(series, freq=30)

result.plot()
pyplot.show()
seasonal = result.seasonal 
seasonal.plot()
pyplot.show()
#pyplot.axis([0,600,0,100])


# In[ ]:




# In[ ]:



