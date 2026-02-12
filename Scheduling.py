#2022-2023 Programação 2
#Grupo 106
#60294 Pedro Rosa
#60285 Tomás Nogueira


from NotAssigned import NotAssigned
from Skippers import Skippers
from Event import Event
from Skipper import Skipper
from Request import Request
from DateTime import Date_toInt,Int_to_Hora,DayTomoroww,HourToMinutes,AfterHour
from copy import deepcopy
from Constants import SKIPPER_ENDDATE_IDX,SKIPPER_ENDHOUR_IDX,SKIPPER_NAME_IDX,SKIPPER_PRICEHOUR_IDX,SKIPPER_HOURSACUMULATED_IDX,SCHEDULE_HOURSNAVEGATION_IDX,SCHEDULE_DATE_IDX,SCHEDULE_HOUR_IDX,SKIPPER_HOURWITHOUTBREAK_IDX

class Scheduling():

    """
    Updates the Schedule
    """

    def __init__(self,skippers,requests,schedule,previousdate,previoushour,starthourheader):

        """
        Creates a objects of skippers, requests, schedule, previous date, previous hour and star hour
        """
        
        self._skippers=skippers
        self._requests=requests
        self._schedule=schedule
        self._previousdate=previousdate
        self._previoushour=previoushour
        self._starthourheader=starthourheader

    def getSkippers(self):

        """
        Gets the skippers of the file
        """

        return self._skippers
    
    def getRequests(self):

        """
        Gets the requests of the file
        """

        return self._requests
    
    def getSchedule(self):

        """
        Gets the schedule of the file
        """

        return self._schedule
    
    def getPreviousdate(self):

        """
        Gets the previous date of the file
        """

        return self._previousdate
    
    def getPreviousHour(self):

        """
        Gets the previous hour of the file
        """

        return self._previoushour
    
    def getStarthourheader(self):

        """
        Gets the start hour header of the file
        """

        return self._starthourheader

    def setSkippers(self,new):

        """
        Set a new skipper 
        """

        self._skippers=new

    def setRequests(self,new):

        """
        Set a new request
        """

        self._requests=new

    def setSchedule(self,new):

        """
        Set a new schedule
        """

        self._schedule=new

    def setStarthourheader(self,new):

        """
        Set a new start hour
        """

        self._starthourheader=new

    def __str__(self):

        """
        Creates a string of objects
        """

        pass

    def __eq__(self,other):

        """
        Compares if there are two files with the same content
        """

        return self.getSkippers()==other.getSkipper() or self.getSchedule()==other.getSchedule() or self.getRequests==other.getRequests()

    def __lt__(self,other):

        """
        Compares if there are a file that starts earlier
        """

        return self.getPreviousdate()<other.getPreviousdate() or self.getPreviousHour()<other.getPreviousHour()

    def Match(self):

        """
        Assigned a request to a skipper that has the requeriments needed for the job

        Requires: list of objects (skipper, schedule and requests)
        Ensures: list of skippers updated and list of events updated
        """

        schedule=deepcopy(self._schedule)
        skippers=deepcopy(self._skippers)
        requests=deepcopy(self._requests)

        to_delete=[]

        for k in range(0, len(schedule)):

            if Date_toInt(schedule[k].getDate()) < Date_toInt(self._previousdate):
                to_delete.append(k)

            elif Date_toInt(schedule[k].getDate())+Date_toInt(schedule[k].getHour())+HourToMinutes(schedule[k].getHoursnavegation()) <= Date_toInt(self._previousdate)+Date_toInt(self._previoushour):
                to_delete.append(k)
        
        for k in sorted(to_delete,reverse=True):

            del(schedule[k])
        
        not_assigned=[]

        for i in range(len(requests)):
            
            skippers_available=[]
            
            for n in range(len(skippers)):

                if skippers[n].getSkipperLevel()==requests[i].getLevel() and skippers[n].getSkipperspecialization()==requests[i].getSpecialization() and\
                (skippers[n].getSkipperLanguage()[0] in requests[i].getLanguage() or \
                skippers[n].getSkipperLanguage()[1] in requests[i].getLanguage() or \
                skippers[n].getSkipperLanguage()[2] in requests[i].getLanguage() or \
                skippers[n].getSkipperLanguage()[3] in requests[i].getLanguage() )and \
                int(skippers[n].getHoursacumulated())+int(requests[i].getHours())<= int(skippers[n].getHourswithoutbreak()):
                    
                    if Date_toInt(skippers[n].getEndhour())+HourToMinutes(requests[i].getHours()) <= 2000:
                        skippers_available.append(skippers[n])
                        skippers_available.sort(key=lambda skippers_available: (skippers_available.getEndhour(), skippers_available.getPricehour(),skippers_available.getHoursacumulated(),skippers_available.getSkipperName() ))

                    else:
                        skippers_available.append(Skipper([skippers[n].getSkipperName(),skippers[n].getSkipperLanguage(),skippers[n].getSkipperLevel(),\
                        skippers[n].getPricehour(),skippers[n].getSkipperspecialization(),skippers[n].getHourswithoutbreak(),skippers[n].getHoursacumulated(),DayTomoroww(skippers[n].getEnddate()),"08:00"]))

                        skippers_available.sort(key=lambda skippers_available: (skippers_available.getEndhour(), skippers_available.getPricehour(),skippers_available.getHoursacumulated(),skippers_available.getSkipperName() ))

            if len(skippers_available)==0:
                not_assigned.append(NotAssigned([self._previousdate,"not-assigned",requests[i].getName()])) 

            else:
                if Date_toInt(skippers_available[0].getEnddate())==Date_toInt(schedule[0].getDate()) and\
                Date_toInt(skippers_available[0].getEndhour())<Date_toInt(AfterHour(self._starthourheader)):
                    
                    skippers_available[0].setEndHour(AfterHour(self._starthourheader))

                schedule.append(Event([skippers_available[0].getEnddate(),skippers_available[0].getEndhour(),requests[i].getHours(),\
                    skippers_available[0].getSkipperName(),int(skippers_available[0].getPricehour())*int(requests[i].getHours()),requests[i].getName()]))
                schedule_new_element=[skippers_available[0].getEnddate(),skippers_available[0].getEndhour(),requests[i].getHours(),\
                    skippers_available[0].getSkipperName(),int(skippers_available[0].getPricehour())*int(requests[i].getHours()),requests[i].getName()]
                
                skippers_available[0].setHoursacumulated(int(skippers_available[0].getHoursacumulated())+int(schedule_new_element[SCHEDULE_HOURSNAVEGATION_IDX]))
                skippers_available[0].setEnddate(""+schedule_new_element[SCHEDULE_DATE_IDX])
                skippers_available[0].setEndHour(Int_to_Hora(Date_toInt(schedule_new_element[SCHEDULE_HOUR_IDX])+(int(schedule_new_element[SCHEDULE_HOURSNAVEGATION_IDX])*100))+"")

                for k in range(0,len(skippers)):

                    if skippers[k].getSkipperName() == skippers_available[0].getSkipperName():
                        skippers[k].setHourswithoutbreak(skippers_available[0].getHourswithoutbreak())
                        skippers[k].setHoursacumulated(skippers_available[0].getHoursacumulated())
                        skippers[k].setEndHour(skippers_available[0].getEndhour())
                        skippers[k].setEnddate(skippers_available[0].getEnddate())

        schedule.sort(key=lambda schedule:(schedule.getDate(),schedule.getHour(),schedule.getSkippersname())) 

        for i in range(0,len(not_assigned)):

            schedule.insert(i,not_assigned[i])
            
        return skippers,schedule    