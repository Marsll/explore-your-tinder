import json
import numpy as np
from datetime import date
from dateutil import relativedelta
import math
from collections import Counter
import codecs

def count(dictionary):
    """Return total number of dictionary entry.
    """
    count = 0
    for key in dictionary:
        count += dictionary[key]
    return count

def create_date(date_str):
    """Return date from string"""
    year = int(date_str[0:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])

    return date(year, month, day)

def cumulate_swipes(swipes):
    """Calculate cumulate swipe count with corresponding dates."""
    dates = []
    swipes_counts = []
    last_count = 0
    for date_str in swipes:
        dates.append(create_date(date_str))
        last_count += swipes[date_str]
        swipes_counts.append(last_count)
    return {"dates": dates, "swipes_count": swipes_counts} 

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
        return f'{months}m {days}d'
    else:
        return f'{years}y {months}m {days}d'


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
    gender = data["User"]["gender"]
    gender_filter = data["User"]["gender_filter"]

    # calculate useful values
    app_opens_total = count(app_opens)
    swipes_likes_total = count(swipes_likes)
    swipes_passes_total = count(swipes_passes)
    matches_total = count(matches)
    messages_sent_total = count(messages_sent)
    messages_received_total = count(messages_recieved)
    counter = Counter
    swipes_cum = cumulate_swipes(counter(swipes_likes) + counter(swipes_passes))
    swipes_likes_cum = cumulate_swipes(counter(swipes_likes))
    matches_cum = cumulate_swipes(counter(matches))
    match_rate_cum = np.array(matches_cum["swipes_count"]) / np.array(swipes_likes_cum["swipes_count"])
  

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
    data_dict["no_match_total"] = no_match
    data_dict["match_rate"] = match_rate
    data_dict["swipes_likes_total"] = swipes_likes_total
    data_dict["swipes_passes_total"] = swipes_passes_total
    data_dict["app_opens_total"] = app_opens_total
    data_dict["messaging"] = messaging
    data_dict["no_messaging"] = no_messaging
    data_dict["messages_sent_total"] = messages_sent_total
    data_dict["messages_received_total"] = messages_received_total
    data_dict["usage_time"] = usage_time
    data_dict["gender"] = gender
    data_dict["gender_filter"] = gender_filter
    data_dict["swipes_cum"] = swipes_cum
    data_dict["swipes_likes_cum"] = swipes_likes_cum
    data_dict["matches_cum"] = matches_cum
    data_dict["matchrate_cum"] = match_rate_cum

    write_messages_txt(data)

    return data_dict

def write_messages_txt(data):
    # TODO look why every line is there twice!
    # overwrite current txt file
    with codecs.open("application/static/data/Messages.txt", "w", "utf-8-sig") as temp:
        temp.write('\n')
    for mes_dict in data["Messages"]:
        for dictionary in mes_dict['messages']:
            with codecs.open("application/static/data/Messages.txt", "a", "utf-8-sig") as temp:
                temp.write(dictionary['message']+'\n')

