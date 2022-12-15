import datetime
import pytz # adds timezones

# naive datestimes, don't have timezones 
# aware datetimes, have timezones

#datetime.date(2022, 12, 15) #YYYY,MM,DD
#datetime.date() # create datetime object
#day # gets the day
#datetime.daytime(1905, 5, 25, 12, 30, 50) #YEAR, MONTH, DAY, HOURS, MINUTES, SECONDS
#d2.weekday() # gets the day from 0-7
#d2.isoweekday() #gets the day from 1-7
#datetime.timedelta(days=7) # timedelta is formatted = '7 days, 0:00:00'
#print(d - delta) # time between two dates
#delta.total_seconds() # total seconds
# 'date - date' results in a timedelta

datetime.datetime(2022, 12, 15, tzinfo=pytz.UTC) # Custom date with timezone
dt_now = datetime.datetime.now(tz=pytz.UTC) # today, allows for timmezone
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC) # UTC time, timezone = none
dt_gmt = dt_now.astimezone(pytz.timezone('Poland'))
dt_gmt.isoformat() # converts to isoformat

dt_str = 'August 19, 2019'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y') # converts strings into datetime using params