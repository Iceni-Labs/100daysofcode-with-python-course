from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    timestamp = line.split()[1]

    extract = re.search('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', line)
    date = datetime.strptime(extract.group(), '%Y-%m-%dT%H:%M:%S')
    return date



def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    dates = []
    for i in range(len(loglines)):
        search = re.search('.+Shutdown initiated', loglines[i])
        if search is not None:
            dates.append(convert_to_datetime(loglines[i]))
    diff = dates[1] - dates[0]
    return diff


print(convert_to_datetime('INFO 2014-07-03T23:27:51 supybot Shutdown complete.'))
print(time_between_shutdowns(loglines))
