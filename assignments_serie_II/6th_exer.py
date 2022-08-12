"""
from 2010 to 2018 group weekdays and weekends in two lists
notes: you are allowed to just use datetime or numpy datetime
"""
import numpy as np

date_time_range = np.arange(np.datetime64('2010-01-04'), np.datetime64('2018-01-01'))
print(date_time_range, type(date_time_range), date_time_range.shape)

t = int(date_time_range.size/7)
date_time_range_new = date_time_range.reshape((t, 7))
print(date_time_range_new.shape)

lst_1 = list(date_time_range_new)
lst_2 = list(date_time_range_new[:, 6])
print(lst_2)


