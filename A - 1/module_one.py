#!/usr/bin/env python
# coding: utf-8

# In[3]:



class module_sublist:
    """This class has a constructor that takes in an integer value that 
    indicates how long of a list is to be constructed at the time an object 
    of this class is created.  There is to be one method that also takes in 
    an integer value that indicates what sized sub-list the method will return. 
    The returned sub-list is constructed from the original list that was 
    stored at the object creation."""
    def __init__(self, l):
        self.l = l
        self.orig_list = list(range(l))
    def sublist(self,x):
        if(x<=self.l):
            sub_list = self.orig_list[0:x]
            return sub_list
        
        
        

        


# In[ ]:





# In[ ]:




