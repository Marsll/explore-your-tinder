import json
import numpy as np
from datetime import date
from dateutil import relativedelta
import math

def count(dictionary):
    """Return total number of dictionary entry.
    """
    count = 0
    for key in dictionary:
        count += dictionary[key]
    return count


def time_difference(date_str):

    year = int(date_str[0:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])
    today = date.today()
    start_date = date(year, month, day)

    diff = relativedelta.relativedelta(today, start_date)

    years = diff.years 
    months = diff.months
    days = diff.days
    if months == 0:
        return f'{days} days'
    elif years == 0:
        return f'{months} months {days} days'
    else:
        return f'{years} years {months} months {days} days'


def get_data(str):
    with open(str, encoding="utf8") as json_file:
        data = json.load(json_file)

    # get data from json
    app_opens = data['Usage']['app_opens']
    swipes_likes = data['Usage']['swipes_likes']
    swipes_passes = data['Usage']['swipes_passes']
    matches = data['Usage']['matches']
    messages_sent = data['Usage']['messages_sent']
    messages_recieved = data['Usage']['messages_received']
    messaging = int(data["Messages"][0]["match_id"][6:])

    # calculate useful values
    app_opens_total = count(app_opens)
    swipes_likes_total = count(swipes_likes)
    swipes_passes_total = count(swipes_passes)
    matches_total = count(matches)
    messages_sent_total = count(messages_sent)
    messages_received_total = count(messages_recieved)

    swipes_total = swipes_likes_total + swipes_passes_total
    no_match = swipes_likes_total - matches_total
    match_rate = math.ceil(matches_total / swipes_likes_total * 100)
    no_messaging = matches_total - messaging

    # calc usage time
    first_open = list(app_opens.keys())[0]
    usage_time = time_difference(first_open)

    # feed data_dict with values
    data_dict = dict()
    data_dict["swipes_total"] = swipes_total
    data_dict["matches_total"] = matches_total
    data_dict["no_match"] = no_match
    data_dict["match_rate"] = match_rate
    data_dict["swipes_likes_total"] = swipes_likes_total
    data_dict["swipes_passes_total"] = swipes_passes_total
    data_dict["app_opens_total"] = app_opens_total
    data_dict["messaging"] = messaging
    data_dict["no_messaging"] = no_messaging
    data_dict["messages_sent_total"] = messages_sent_total
    data_dict["messages_received_total"] = messages_received_total
    data_dict["usage_time"] = usage_time

    return data_dict

