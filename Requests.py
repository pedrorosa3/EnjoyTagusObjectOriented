#2022-2023 Programação 2
#Grupo 106
#60294 Pedro Rosa
#60285 Tomás Nogueira


from Request import Request
from Constants import NUM_HEADER_LINES

class Requests:

    """
    Create a object that contains a list of objects with the requests
    """

    def __init__(self,filename):

        """
        List with request objects

        Requires: filename is a .txt file
        Ensures: list with request objects
        """

        self._filename=filename

    def getFileName(self):

        """
        Get the filename
        """

        return self._filename

    def ReadFileRequest(self):

        """
        Read the file and save the informations of the elements in a list of lists

        Requires: file is a .txt file
        Ensures: list of lists that contains informations os the requests
        """

        list=[]
        
        try:
            file=open(self.getFileName(),"r")
        except FileNotFoundError:
            print("Could not found this file")
            file.close()
        finally:

            for line in file.readlines()[7:]:
                list.append(line)
            file.close()  
    
            requests = [] 

            for line in list:
                requestData = (line.rstrip().split(", "))
                requestData[1]=(requestData[1]).split("; ")

                for i in range(0, len(requestData[1])):
                        requestData[1][i]=requestData[1][i].replace("(","").replace(")","")
                requests.append(requestData)        
    
        return requests

    def GetHeader(self):

        """
        Read the file and save the information of the header in a list 

        Requires: filename is a .txt file
        Ensures: List with the information of the header
        """

        header=[]

        try:
            file=open(self._filename,"r")
        except FileNotFoundError:
            print("Could not found this file")
            file.close()
        finally:

            for line in file.readlines()[:NUM_HEADER_LINES]:
                header.append(line)
            file.close()  

        for n in range(len(header)):
            header[n]=header[n].rstrip()

        return header

    def ObjectsRequest (self):

        """
        Convert Lists of lists to a list of objects 

        Requires: list of list with informations about the requests
        Ensures: list of  request objects  
        """

        objectsrequests=[]
        
        for i in range(len(self.ReadFileRequest())):
            objectsrequests.append(Request(self.ReadFileRequest()[i]))

        return objectsrequests    