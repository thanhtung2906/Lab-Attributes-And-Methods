import math 
class Integer:
    def __init__(self,value:int):
        self.value = value
    @classmethod
    def from_float(cls,value):
        if isinstance(value,float):
            floor = math.floor(value)
            return cls(floor)
        else:
            return 'value is not a float'
    @classmethod
    def from_roman(cls,value):    
        roman = {'I':1,'IV':4,'V':5,'IX':9,'X':10}
        i = 0
        num = 0
        while i < len(value):
            if i+1<len(value) and value[i:i+2] in roman:
                num += roman[value[i:i+2]]
                i += 2
            else:
                num += roman[value[i]]
                i += 1
        return cls(num)
    @classmethod    
    def from_string(cls,value):
        if isinstance(value,str):
            return cls(int(value))
        else:
            return 'wrong type'

    def add(self,integer:int):
        if isinstance(integer,Integer):
            self.value += integer.value
            return self.value
        else: 
            return 'Can only add Integer instance'
    def __add__(self,other):
        if isinstance(other,Integer):
            return Integer(self.value + other.value)
        else:
            return 'Can only add Integer instance'
           
    def __repr__(self):
        return f"Integer({self.value})"
  
first_num = Integer(10)
second_num = Integer.from_roman("IV")
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num + second_num)