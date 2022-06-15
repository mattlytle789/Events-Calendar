# File to hold all of the variables being used in the Events Calendar program

# Variables input from user 
locationRequest = '' # Location to search at for events					: format City,State
startDateRequest = '000000' # start date to search during for events	: format mmddyy
endDateRequest = '000000' # end date to search during for events		: format mmddyy

# Internal variables 
eventsList = [] # list to hold the name of all events 
eventsDict = {} # dictionary to hold the event name and date			: format {'name', 'date'}
