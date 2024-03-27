class Lake:
    def __init__(self, name, location, depth, width, size, type ):
        self.name = name
        self.location = location
        self.depth = depth
        self.width = width
        self.size = size
        self.ltype = ltype  
#shish method(__init__) is a special method used to identify properties of a class
# the first parameter in the shish parenthesis refers to an individual property of a class/objects and not an attribute
  
#creating objects of a class Lake
lake1 = Lake("L.victoria", "entebbe", "1400ft", "550m", "700m", "salty") 

 

    


class River:
    def __init__(self, a, b, c):
        self.name = a
        self.location = b
        self.length = c
#any method of a class should take a parameter "self"        
river1 = River("R.Nile", "jinja", "600km")
