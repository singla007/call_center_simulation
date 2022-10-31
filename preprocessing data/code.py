import pandas as pd
from datetime import date, time


data = pd.read_csv("Raw data\simulated_call_centre.csv")[:1000]

print(data.columns)

data = data.drop(['daily_caller', 'call_answered',
       'call_ended', 'wait_length', 'meets_standard'], axis=1)

print(data.columns)

# Finding Arrival times
data['call_started_24hr'] = pd.to_datetime(data['call_started'])
print(data['call_started_24hr'].dt.strftime('%H:%M:%S').str)
data['arrival_time'] = data['date'] +" " + data['call_started_24hr'].dt.strftime('%H:%M:%S')
# data['arrival_time'] = pd.to_datetime(data['date'], format='%Y-%m-%d') + data['call_started_24hr']
# print(pd.to_datetime(data['date'], format='%Y-%m-%d'))
# print(data['call_started_24hr'])
data['arrival_time'] = pd.to_datetime(data['arrival_time'])

# print(date(int(data['date'][0])))
# ts = pd.Timestamp.combine(date(data['date'][0]), time(data['call_started'][0]))
# print(ts)
# Finding Interarrival times
interarrival_time = list()
interarrival_time.append(pd.Timedelta(data['arrival_time'][0]-data['arrival_time'][0]))
for i in range(data.shape[0]-1):
    interarrival_time.append(pd.Timedelta(data['arrival_time'][i+1]-data['arrival_time'][i]))

interarrival_time_sec = list()    
for i in interarrival_time:
    interarrival_time_sec.append(int(i.total_seconds()/60))
# print(interarrival_time_sec)
data['interarrival_time'] = interarrival_time_sec

service_time = list()
for i in data['service_length']:
    service_time.append(int(i/60))
data['service_length'] = service_time
# print(service_time)

data = data.drop(['date', 'call_started', 'call_started_24hr'], axis=1)
print(data.columns)

server1_data = data.iloc[:150]
server2_data = data.iloc[200:350]
server3_data = data.iloc[400:550]
server4_data = data.iloc[600:750]

server1_data.to_csv("processed_data\server1_data.csv", index=False)
server2_data.to_csv("processed_data\server2_data.csv", index=False)
server3_data.to_csv("processed_data\server3_data.csv", index=False)
server4_data.to_csv("processed_data\server4_data.csv", index=False)

# Statistics

# Average range of service time for server 1
print("Max and min range of service time in seconds for server 1", max(server1_data['service_length']), min(server1_data['service_length']))

# Average range of service time for server 2
print("Max and min range of service time in seconds for server 2", max(server2_data['service_length']), min(server2_data['service_length']))

# Average range of service time for server 3
print("Max and min range of service time in seconds for server 3", max(server3_data['service_length']), min(server3_data['service_length']))

# Average range of service time for server 4
print("Max and min range of service time in seconds for server 4", max(server4_data['service_length']), min(server4_data['service_length']))

print("Average service time for server 1",sum(server1_data['service_length'])/150)
print("Average service time for server 3",sum(server3_data['service_length'])/150)
print("Average service time for server 4",sum(server4_data['service_length'])/150)


print("server1 **********************************************")
freq_dist = dict()
for i in server1_data['interarrival_time']:
    # i= int(i.total_seconds()/60)
    if i in freq_dist.keys():
        freq_dist[i] += 1
    else:
        freq_dist[i] = 1

print(len(freq_dist))
print(freq_dist)

print("Probability")
total_prob = 0
for key in freq_dist.keys():
    print(key,freq_dist[key]/len(server1_data['interarrival_time']))
    total_prob += freq_dist[key]/len(server1_data['interarrival_time'])

print(total_prob)

print("server2 **********************************************")
freq_dist = dict()
for i in server2_data['interarrival_time']:
    # i= int(i.total_seconds()/60)
    if i in freq_dist.keys():
        freq_dist[i] += 1
    else:
        freq_dist[i] = 1

print(len(freq_dist))
print(freq_dist)

print("Probability")
total_prob = 0
for key in freq_dist.keys():
    print(key,freq_dist[key]/len(server2_data['interarrival_time']))
    total_prob += freq_dist[key]/len(server2_data['interarrival_time'])

print(total_prob)

print("server3 **********************************************")
freq_dist = dict()
for i in server3_data['interarrival_time']:
    # i= int(i.total_seconds()/60)
    if i in freq_dist.keys():
        freq_dist[i] += 1
    else:
        freq_dist[i] = 1

print(len(freq_dist))
print(freq_dist)

print("Probability")
total_prob = 0
for key in freq_dist.keys():
    print(key,freq_dist[key]/len(server3_data['interarrival_time']))
    total_prob += freq_dist[key]/len(server3_data['interarrival_time'])

print(total_prob)

print("server4 **********************************************")
freq_dist = dict()
for i in server4_data['interarrival_time']:
    # i= int(i.total_seconds()/60)
    if i in freq_dist.keys():
        freq_dist[i] += 1
    else:
        freq_dist[i] = 1

print(len(freq_dist))
print(freq_dist)

print("Probability")
total_prob = 0
for key in freq_dist.keys():
    print(key,freq_dist[key]/len(server4_data['interarrival_time']))
    total_prob += freq_dist[key]/len(server4_data['interarrival_time'])

print(total_prob)