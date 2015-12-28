
import arcpy
import datetime

tc = "d:\\temp\\tc.shp"

##search cursor list of dates where setyear is blank
dates = [i for i, in arcpy.da.SearchCursor
       (tc,"SETDATE",'CHAR_LENGTH("SETYEAR")=1') if i != None]

for date in dates:
    date.strftime("%Y")
    print date

##
##with arcpy.da.UpdateCursor(tc,["SETDATE","SETYEAR"],'CHAR_LENGTH("SETYEAR")=1') as yearcursor:
##    for row in yearcursor:
##
##        datetime.strftime("%m/%d/%Y")[-4]
####        yearcursor.updateRow()
##del yearcursor