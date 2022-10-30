import pandas as pd
from datetime import date, time


data = pd.read_csv("Raw data\simulated_call_centre.csv")

print(data.columns)

data = data.drop(['daily_caller', 'call_answered',
       'call_ended', 'wait_length', 'meets_standard'], axis=1)

print(data.columns)

data['call_started_24hr'] = pd.to_datetime(data['call_started'])
print(data['call_started_24hr'].dt.strftime('%H:%M:%S').str)
data['arrival_time'] = data['date'] +" " + data['call_started_24hr'].dt.strftime('%H:%M:%S')
# data['arrival_time'] = pd.to_datetime(data['date'], format='%Y-%m-%d') + data['call_started_24hr']
# print(pd.to_datetime(data['date'], format='%Y-%m-%d'))
# print(data['call_started_24hr'])
print(pd.to_datetime(data['arrival_time']))

# print(date(int(data['date'][0])))
# ts = pd.Timestamp.combine(date(data['date'][0]), time(data['call_started'][0]))
# print(ts)