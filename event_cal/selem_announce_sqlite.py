import os
import sys
import time
import sqlite3
import datetime
import json
import uuid
import requests
from pytz import timezone as tz

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
PATH_TO_DB = sys.argv[1]

SELEM_ANNOUCE_GROUP_ID = "22655581"
# BOTNET_GROUP_ID = '52108754'
ACCESS_TOKEN = "VnGXCbwtEeOYiaWAwtY52QEsN1BdlxO9AleqW73Q"
CREATE_MESSAGE_URL = "https://api.groupme.com/v3/groups/%s/messages?token=%s" % (SELEM_ANNOUCE_GROUP_ID, ACCESS_TOKEN)
# CREATE_MESSAGE_URL = "https:/ /api.groupme.com/v3/groups/%s/messages?token=%s" % (BOTNET_GROUP_ID, ACCESS_TOKEN)

conn = sqlite3.connect(PATH_TO_DB)
c = conn.cursor()
c.execute('SELECT * FROM web_cal_event ORDER BY event_datetime ASC;')
event_list = c.fetchall()

def has_occured(event):
    event_start_time = datetime.datetime.strptime(event[2], TIME_FORMAT)
    event_start_time = event_start_time.replace(tzinfo=tz('UTC'))
    current_time = datetime.datetime.utcnow().replace(tzinfo=tz('UTC'))
    if current_time > event_start_time:
        return True
    else:
        return False

def should_announce(event):
    announce_delta = datetime.timedelta(minutes=10)
    event_start_time = datetime.datetime.strptime(event[2], TIME_FORMAT)
    event_start_time = event_start_time.replace(tzinfo=tz('UTC'))
    current_time = datetime.datetime.utcnow().replace(tzinfo=tz('UTC'))
    if (event_start_time - announce_delta) < current_time < event_start_time:
        return True
    else:
        return False

def announce(event):
    message_uuid = uuid.uuid4()
    event_name = event[1]
    event_time = datetime.datetime.strptime(event[2], TIME_FORMAT).replace(tzinfo=tz('UTC'))
    event_time = event_time.astimezone(tz('US/Eastern')).strftime('%I:%M%p')
    event_location = event[3]
    message_text = '{event_name} ({event_time}) @ {event_location}'.format(event_name=event_name, 
                                                                           event_time=event_time, 
                                                                           event_location=event_location)

    post_data = {"message": {"source_guid": str(message_uuid), "text": message_text}}
    headers = {"Content-Type": "application/json"}
    # retry up to 3 times
    for i in range(3):
        r = requests.post(CREATE_MESSAGE_URL, data=json.dumps(post_data), headers=headers)
        print(r)
        print(r.content)
        if r.status_code == 201:
            break

while len(event_list) > 0:
    if has_occured(event_list[0]) == True:
        event_list.pop(0)
    elif should_announce(event_list[0]) == True:
        announce(event_list[0])
        event_list.pop(0)
    else:
        time.sleep(60)
