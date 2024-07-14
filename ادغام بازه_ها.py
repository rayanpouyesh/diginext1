#!/usr/bin/env python
# coding: utf-8

# In[4]:


def mergeIntervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]

        if current[0] <= last_merged[1]:
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            merged.append(current)

    return merged

intervals = [(1, 3), (2, 6), (8, 10)]
print(mergeIntervals(intervals)) 


# In[ ]:




