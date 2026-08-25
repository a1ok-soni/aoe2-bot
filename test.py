from datetime import datetime
import pytz
print(' '.join(pytz.country_timezones['in']))
tz_IN = pytz.timezone('Asia/Kolkata')
datetime_IN = datetime.now(tz_IN)
print("Time: ", datetime_IN)
