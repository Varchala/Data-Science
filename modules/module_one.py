class module_one:
    """This class has a constructor that takes in an integer value that 
    indicates how long of a list is to be constructed at the time an object 
    of this class is created.  There is to be one method that also takes in 
    an integer value that indicates what sized sub-list the method will return. 
    The returned sub-list is constructed from the original list that was 
    stored at the object creation."""
    def __init__(self, length, x):
        self._length = length
        self.orig_list = x[:]
    def sublist(self,x):
        if(x<=self.length):
            sub_list = self.orig_list[1:x]
            return sub_list
        else:
            print("The length of sublist should not exceed the length of original list")
            
        
        
        

        
