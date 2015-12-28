import arcpy
from datetime import datetime 	#import the datetime class from the datetime module

tc = "d:\\temp\\tc.shp"
fields = ["SETDATE", "SETYEAR"]

## either of these clauses should work if you are testing for a field not set
where = 'char_length("SETYEAR") = 1'
#where = '"SETYEAR"' + " < '1900'"

with arcpy.da.UpdateCursor(tc, fields, where) as yearcursor:
	for row in yearcursor:
		set_date = row[0] 	#get the SETDATE field value
		
		set_year = datetime.strftime(set_date, "%Y")  	#use datetime to create string of year 

		## add your udpate field/row functionality

del yearcursor


##
##with arcpy.da.UpdateCursor(tc,["SETDATE","SETYEAR"],'CHAR_LENGTH("SETYEAR")=1') as yearcursor:
##    for row in yearcursor:
##
##        datetime.strftime("%m/%d/%Y")[-4]
####        yearcursor.updateRow()
##del yearcursor