#2022-2023 Programação 2
#Grupo 106
#60294 Pedro Rosa
#60285 Tomás Nogueira


class Skipper:

    """
    Save the informations of the skippers
    """

    def __init__(self,elem):

        """
        Create a skipper
        """

        self._skippername=elem[0]
        self._skipperlanguage=elem[1]
        self._skipperlevel=elem[2]
        self._pricehour=elem[3]
        self._skipperspecialization=elem[4]
        self._hourswithoutbreak=elem[5]
        self._hoursacumulated=elem[6]
        self._enddate=elem[7]
        self._endhour=elem[8]
    
    def getSkipperName(self):

        """
        Gets the skipper name
        """

        return self._skippername
    
    def getSkipperLanguage(self):

        """
        Gets the skipper language
        """

        return self._skipperlanguage
    
    def getSkipperLevel(self):

        """
        Gets the skipper level
        """

        return self._skipperlevel
    
    def getPricehour(self):

        """
        Gets the price hour of a skipper
        """

        return self._pricehour
    
    def getSkipperspecialization(self):

        """
        Gets the specialization of the skipper
        """

        return self._skipperspecialization
    
    def getHourswithoutbreak(self):

        """
        Gets the hours without a break of a skipper
        """

        return self._hourswithoutbreak
    
    def getHoursacumulated(self):

        """
        Gets the hours acumulated of a skipper
        """

        return self._hoursacumulated
    
    def getEnddate(self):

        """
        Gets the end of the date of the final service
        """

        return self._enddate
    
    def getEndhour(self):

        """
        Gets the end of the hour of the final service
        """

        return self._endhour
    
    def setName(self,new):

        """
        Set a new name to a skipper
        """
        
        self._name=new

    def setLanguage(self, new):

        """
        Set a new language to a skipper
        """

        self._language=new
    
    def setPricehour(self, new):

        """
        Set a new price hour to a skipper
        """

        self._pricehour=new

    def setSkipperspecialization(self, new):

        """
        Set a new specialization of a skipper
        """

        self._specialization=new
    
    def setHourswithoutbreak(self,newhours):

        """
        Set a new hours without a break of a skipper
        """

        self._hourswithoutbreak=newhours

    def setHoursacumulated(self,newhours):

        """
        Set a new hours acumulated of a skipper
        """

        self._hoursacumulated=newhours

    def setEnddate(self,newhours):

        """
        Set a new end date of a skipper
        """

        self._enddate=newhours

    def setEndHour(self,newhours):

        """
        Set a new end hour of a skipper
        """

        self._endhour=newhours  

    def SkipperConvert(self):

        """
        Creates a list of objects
        """

        return [self.getSkipperName(),self.getSkipperLanguage(),self.getSkipperLevel(),self.getPricehour(),self.getSkipperspecialization(),self.getHourswithoutbreak(),self.getHoursacumulated(),self.getEnddate(),self.getEndhour()]        

    def __str__(self):

        """
        Creates a string of objects
        """

        return self.getSkipperName() + ","+ str(self.getSkipperLanguage()) + ","+ str(self.getSkipperLevel()) +","+str(self.getPricehour()) + ","+self.getSkipperspecialization() +","+str(self.getHourswithoutbreak())+","+str(self.getHoursacumulated())+","+self.getEnddate()+","+self.getEndhour() 

    def __eq__(self,other):

        """
        Compares if there are two skippers with the same name
        """

        return self.getSkipperName()==other.getSkipperName()
    
    def __lt__(self,other):

        """
        Compares the end hour of two skippers
        """

        return self.getEndhour()<other.getEndhour()