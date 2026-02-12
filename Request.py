#2022-2023 Programação 2
#Grupo 106
#60294 Pedro Rosa
#60285 Tomás Nogueira


class Request:

    """
    Create a request object
    """

    def __init__(self,elem):

        """
        Create a request
        
        Request: elem is a list with details of the request
        Ensures: Object with the details of the requet
        """

        self._elem=elem
        self._name=elem[0]
        self._language=elem[1]
        self._level=elem[2]
        self._specialization=elem[3]
        self._hours=elem[4]

    def getName(self):
        
        """
        Get the name of the request
        """

        return self._name
    
    def SetName(self,new):

        """
        Set a new name of the request
        """

        self._name=new

    def getLanguage(self):

        """
        Get the language of the request
        """

        return self._language
    
    def SetLanguage(self,new):

        """
        Set a new language of the request
        """

        self._language=new

    def getLevel(self):

        """
        Get  level of the request
        """

        return self._level
    
    def SetLevel(self,new):

        """
        Set a new level of the request
        """

        self._level=new

    def getSpecialization(self):

        """
        Get the specialization of the request 
        """

        return self._specialization
    
    def SetSpecialization(self,new):

        """
        Set a new specialization of the request
        """

        self._specialization=new

    def getHours(self):

        """
        Get the hours language of the request
        """

        return self._hours
    
    def SetHours(self,new):

        """
        Set a new hours of the request
        """

        self._hours=new

    def __eq__ (self,other):

        """
        Compares the name of 2 given requests 
        """

        return self.getName()==other.getName() 

    def __lt__(self,other):

        """
        Compares witch of the requests has less hours
        """
        return self.getHours()<other.getHours()

    def __str__(self):

        """
        Convert the object to a string 
        """

        return self.getName()+","+str(self.getLanguage())+","+self.getLevel()+","+self.getSpecialization()+","+self.getHours() 