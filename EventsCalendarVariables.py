# File to hold all of the variables being used in the Events Calendar program

# Variables input from user 
locationRequest = "" # Location to search at for events					: format City,State
startDateRequest = "000000" # start date to search during for events	: format mmddyy
endDateRequest = "000000" # end date to search during for events		: format mmddyy

# Event class to hold data about a specific event
class Event:
	date = "000000" # the date of the event								: format mmddyy
	day = "" # day of the week the event is  on
	location = "" # location of the event								: format Venue - City,State
	price = 0 # price of the event
	type = "" # type of event, i.e. concert, movie, festival
