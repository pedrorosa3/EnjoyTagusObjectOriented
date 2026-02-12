#2022-2023 Programação 2
#Grupo 106
#60294 Pedro Rosa
#60285 Tomás Nogueira


from Skipper import Skipper
from Request import Request
from Event import Event
from Constants import HEADER_SPECIFICATION,NUM_HEADER_LINES,HEADER_HOUR_IDX,HEADER_DATE_IDX
from DateTime import AfterHour,DayTomoroww


class Skippers():

    """
    Creates a object collection of skippers, requests and schedule and append in 3 different lists
    """

    def __init__(self,filename):

        """
        Creates an object of the file name
        """
    
        self._filename=filename
      

    def getFileName(self):

        """
        Gets the file name
        """

        return self._filename
    
    def setFileName(self,new):

        """
        Set a new file name
        """

        self._filename=new
    
    def __str__(self):

        """
        Creates a string of objects
        """

        pass

    def __eq__(self,other):

        """
        Compares if there are two files with the same content
        """

        return self.getFileName()==other.getFileName()

    def __lt__(self,other):

        """
        Compares if there are a file that starts earlier
        """

        pass
    
    def ReadFileSkipper(self):

        """
        Reads .txt file and creates a list of the schedule

        Requires: a .txt file
        Ensures: a list of lists
        """

        list=[]

        try:
            file=open(self._filename,"r")
        except FileNotFoundError:
            print("Could not found this file")
            file.close()
        finally:
        
            for line in file.readlines()[7:]:
                list.append(line)
            file.close()

            skippers=[]
    
            for line in list:
                list_skippers=(line.rstrip().split(", "))
                list_skippers[1]=list_skippers[1].split("; ")
                list_skippers[7]=list_skippers[7].replace("(","")
                list_skippers[8]=list_skippers[8].replace(")","")

                for i in range(0,len(list_skippers[1])):
                 list_skippers[1][i]=list_skippers[1][i].replace("(","").replace(")","")  
            
                skippers.append(list_skippers)

            return skippers
   
    def GetHeader(self):

        """
        Read the file and save the information of the header in a list 

        Requires: filename is a .txt file
        Ensures: list with the information of the header
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
    
    def ObjectsSkippers(self):

        """
        Creates a list of objects of the schedule

        Requires: a list of strings
        Ensures: a list of objects
        """

        objectsskippers=[]

        for i in range(len(self.ReadFileSkipper())):

            objectsskippers.append(Skipper(self.ReadFileSkipper()[i]))

        return objectsskippers

    def writeSkippers(self,header,listupdated):

        """
        Writes the objects of the list into a .txt file

        Requires: list of objects
        Ensures: .txt file
        """

        hours_name=AfterHour(header[HEADER_HOUR_IDX]).replace(":","h")
        hours=AfterHour(header[HEADER_HOUR_IDX])

        if hours=="08:00" :
        
            day=DayTomoroww(header[HEADER_DATE_IDX])
        else:

            day=header[HEADER_DATE_IDX]

        fileName="skippers"+hours_name+".txt"
        header="Company:\n"+"Tagus Sailing\n"+"Day:\n"+day+"\n"+"Time:\n"+hours+"\n"+"Skippers:\n" 

        InFile1=open(fileName,"w")
                                                         
        InFile1.write(header)

        for text in listupdated:
            
            text=text.SkipperConvert()
            
            for x in text:
                     
                if type(x)==list:
                    
                    x=str(x).replace(',', ';').replace("'", '').replace('[', '(').replace(']', ')') + ', '
                    InFile1.write(x)

                else:
                    if str(x) == text[-2]:
                        x = "(" + str(x)
                    elif str(x) == text[-1]:
                        x = str(x) + ")"
                        InFile1.write(x)
                        continue

                    x = str(x)+", "
                    InFile1.write(x)
        
            InFile1.write("\n")

        InFile1.close
        
        return InFile1          