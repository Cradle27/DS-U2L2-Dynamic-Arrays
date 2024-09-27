# Conner Radle
# U2L2
import ctypes

class DynamicArray:
  
  def __init__(self):                                                                                  

    self.__n = 0
    self.__capacity = 1
    self.__A = self.__make_array(self.__capacity)

  def __str__(self):
    if self.__n == 0:
        return "[]"

    out = '['
    for i, element in enumerate(self.__A):
        try:
            out += str(element) + ', '
            temp = self.__A[i+1]
        except:
            break
    return out[:-2] + ']'

  def __make_array(self, c):
    """return new array with capacity c"""
    return (c * ctypes.py_object)()

  def __getitem__(self, k):
    """return element at index"""
    if k <= 0 or k >= self.__n:
        raise IndexError("invalid index")
    
    return self.__A[k]

  def get_cap(self):
    return self.__capacity

  def __len__(self):
    return self.__n

  def append(self, item):
    if self.__n == self.__capacity:
      self.__resize()
    self.__n += 1
    self.__A[self.__len__() - 1] = item

  def __resize(self):
    self.__capacity *= 2
    templist = self.__make_array(self.__capacity)
    for i in range(self.__n):
      templist[i] = self.__A[i]
    self.__A = templist
