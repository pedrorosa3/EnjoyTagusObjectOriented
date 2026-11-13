# 2022-2023 Programação 2
# Grupo 106
# 60294 Pedro Rosa
# 60285 Tomás Nogueira

from Constants import HEADER_DATE_IDX,HEADER_HOUR_IDX,HEADER_SPECIFICATION

from DateTime import FileNameToHour,FileNameToSpecification,AfterHour

from Skippers import Skippers

from Event import Event

from Requests import Requests

from Skipper import Skipper

from Request import Request

from Schedule import Schedule

from Scheduling import Scheduling

import sys

skippers=sys.argv[1]
schedule=sys.argv[2]
requests=sys.argv[3]

def assign (skippersFileName, scheduleFileName, requestsFileName):
        
        """
        Run the enjoyTagus aplication

        Requires: 3 .txt files
        Ensures: 2 .txt updated files
        """

        skipperscol=Skippers(skippersFileName)
        skippers=skipperscol.ObjectsSkippers()
        requestscol=Requests(requestsFileName)
        requests=requestscol.ObjectsRequest()
        schedulecol=Schedule(scheduleFileName)
        elements=schedulecol.ObjectsSchedule()
        previousdate=skipperscol.GetHeader()[HEADER_DATE_IDX]
        previoushour=skipperscol.GetHeader()[HEADER_HOUR_IDX]
        header=skipperscol.GetHeader()
        header2=schedulecol.GetHeader()
        header3=requestscol.GetHeader()
        new=Scheduling(skippers,requests,elements,previousdate,previoushour,previoushour)
        new_skippers,new_schedule=new.Match()
       
        header_new1=header[HEADER_SPECIFICATION]
        header_new2=header2[HEADER_SPECIFICATION]
        header_new3=header3[HEADER_SPECIFICATION]
        InFile1=skipperscol.writeSkippers(header,new_skippers)
        InFile2=schedulecol.writeSchedule(header2,new_schedule)

        if header[HEADER_HOUR_IDX]!= FileNameToHour(skippersFileName)or header[HEADER_HOUR_IDX]!= FileNameToHour(requestsFileName) or header[HEADER_HOUR_IDX]!= FileNameToHour(scheduleFileName) or\
        header_new1!= FileNameToSpecification(skippersFileName) or  header_new3!= FileNameToSpecification(requestsFileName) or  header_new2!= FileNameToSpecification(scheduleFileName):
            
            raise Exception("Input file error: scope or time inconsistency between name and header in file <name of file>")
        else:

            return InFile1,InFile2
    
print(assign(skippers,schedule,requests))