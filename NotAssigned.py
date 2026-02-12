#2022-2023 Programação 2
#Grupo 106
#60294 Pedro Rosa
#60285 Tomás Nogueira


class NotAssigned:

    """
    Save the information of the not assigned requests
    """

    def __init__(self,elem):

        """
        Creates a not assigned
        """

        self._elem=elem
        self._previousdate=elem[0]
        self._notassigned=elem[1]
        self._requestsname=elem[2]

    def getPreviousdate(self):

        """
        Get previous date of the file
        """

        return self._previousdate
    
    def setPreviousdate(self,new):

        """
        Set a new previous date
        """

        self._previousdate=new

    def getNotassigned(self):

        """
        Get the not assigned request of the schedule
        """

        return self._notassigned
    
    def setNotassigned(self,new):

        """
        Set a new not assigned
        """

        self._notassigned=new

    def getRequestsname(self):

        """
        Get the request name of the requests
        """

        return self._requestsname
    
    def setRequestsname(self,new):

        """
        Set a new request name
        """

        self._requestsname=new

    def NotConvert(self):

        """
        Converts the objects into a list of objects
        """

        return [self.getPreviousdate(),self.getNotassigned(),self.getRequestsname()]
    
    def __str__(self):

        """
        Convert the objects of the not assigned into a line of the file
        """

        return self.getPreviousdate()+","+self.getNotassigned()+","+self.getRequestsname()
    
    def __eq__(self,other):

        """
        Compares if there are two not assigned similar
        """

        return self.getNotassigned()==other.getNotAssigned()

    def __lt__(self,other):

        """
        Compares which of the events happend earlier
        """

        return self.getPreviousdate()<other.getPreviousdate()