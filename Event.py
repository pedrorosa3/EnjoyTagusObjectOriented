#2022-2023 Programação 2
#Grupo 106
#60294 Pedro Rosa
#60285 Tomás Nogueira


class Event:

    """
    Save the informations of the schedules
    """

    def __init__(self,elem):

        """
        Create a Schedule
        """

        self._date=elem[0]
        self._hour=elem[1]
        self._hoursnavegation=elem[2]
        self._skippersname=elem[3]
        self._price=elem[4]
        self._clientname=elem[5]

    def getDate(self):

        """
        Get date of the file
        """

        return self._date
    
    def setDate(self,new):

        """
        Set a new date
        """

        self._date=new

    def getHour(self):

        """
        Get hour of the file
        """

        return self._hour
    
    def setHour(self, new):

        """
        Set a new hour
        """

        self._hour=new
    
    def getHoursnavegation(self):

        """
        Get hours of navigation of the schedule 
        """

        return self._hoursnavegation
    
    def setHoursnavegation(self, new):

        """
        Set a new hours of navegation
        """
        self._hoursnavegation=new
    
    def getSkippersname(self):

        """
        Get skipper name of the schedule
        """

        return self._skippersname
    
    def setSkippersname(self, new):

        """
        Set a new skippers name
        """

        self._skippersname=new
    
    def getPrice(self):

        """
        Get price of the schedule
        """

        return self._price
    
    def setPrice(self,new):
        
        """
        Set a new price
        """

        self._price=new
    
    def getClientname(self):

        """
        Get client name of the schedule
        """

        return self._clientname
    
    def setClientname(self,new):

        """
        Set a new client name
        """

        self._clientname=new

    def ScheduleConvert(self):

        """
        Convert the objects of the schedule into a list of objects
        """

        return [self.getDate(),self.getHour(),self.getHoursnavegation(),self.getSkippersname(),self.getPrice(),self.getClientname()]        
 
    def __str__(self):

        """
        Convert the objects of the schudele into a line of the file
        """

        return self.getDate()+","+self.getHour()+","+str(self.getHoursnavegation())+","+self.getSkippersname()+","+str(self.getPrice())+","+self.getClientname()    

    def __eq__(self, other):

        """
        Compares clients names
        """

        return self.getClientname()==other.getClientname()

    def __lt__(self,other):

        """
        Compares which of the events happend earlier
        """

        return self.getDate()<other.getDate()