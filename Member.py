class Member():
    def __init__(self, id, name, email, tier, points):
        self.__id = id 
        self.__name = name
        self.__email = email
        self.__tier = tier
        self.__points = points

    # Get and Set Methods
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id 

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name 
    
    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email

    def getTier(self):
        return self.__tier
    
    def setTier(self, tier):
        self.__tier = tier 

    def getPoints(self):
        return self.__points
    
    def setPoints(self, points):
        self.__points = points