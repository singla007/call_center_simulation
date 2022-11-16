import sys
import pandas as pd
import datetime
import Customer as cust
import Server as serv
# from collections import deque

# def arrival_event():
#     pass

# def departure_event1():
#     pass


# class CallCenterSimulation:
#     @staticmethod
def call_centre():
    server1 = serv.Server()
    server2 = serv.Server()
    waiting_queue1 = []
    record = ""
    total_server1_idle_time = 0
    total_server2_idle_time = 0
    Server1_available = False
    Server2_available = False
    total_wait_time = 0
    # total_service_time_at_server_1 = 0
    # total_service_time_at_server_2 = 0
    # totalWaitingTime_at_server1 = 0
    format = "%Y-%m-%d %H:%M:%S"
    server1_data = pd.read_csv("./processed_data/server1_data.csv")
    server2_data = pd.read_csv("./processed_data/server2_data.csv")
    server1_service_time = list(server1_data['service_length'])
    server2_service_time = list(server2_data['service_length'])
    customer_arrival_time = list(server1_data['interarrival_time'])
    customer_index = 0
    service_index = 0
    custom_timer = 0
    while True:
        # Customer arrival
        total_wait_time += len(waiting_queue1)
        if custom_timer >= customer_arrival_time[customer_index]:
            waiting_queue1.append(customer_index)
            customer_index += 1
        if not server1.is_busy and not server2.is_busy and len(waiting_queue1):
            server1.set_curr_service_end_at = custom_timer + server1_service_time[service_index] + server2_service_time[service_index]
            server2.set_curr_service_end_at = custom_timer + server1_service_time[service_index] + server2_service_time[service_index]
            total_server1_idle_time = server1.set_curr_service_end_at - server1_service_time[service_index]
            total_server2_idle_time = server2.set_curr_service_end_at - server2_service_time[service_index]
            waiting_queue1.pop(0)
            service_index += 1
        if server1.get_curr_service_end_at() <= custom_timer:
            server1.is_busy = False
        if server2.get_curr_service_end_at() <= custom_timer:
            server2.is_busy = False
        if customer_index >= server1_data.shape[0]:
            break
        custom_timer += 1 
    print(total_server1_idle_time)
    print(total_server2_idle_time)


call_centre()
# class CallCenterSimulation:
#     @staticmethod
#     def main():
#         server1=serv.Server()
#         server2=serv.Server()
#         waiting_queue1=[]
#         record = ""
#         total_server1_idle_time = 0
#         total_server2_idle_time = 0
#         Server1_available=False
#         Server2_available=False
#         wait_time=0
#         total_service_time_at_server_1 = 0
#         total_service_time_at_server_2 = 0
#         totalWaitingTime_at_server1 = 0
#         format = "%Y-%m-%d %H:%M:%S"
#         outRes = open("./data/results/output_result.csv", 'w')
#         outRes.write("customerId,InterArrivalTime_at_server1,arrivalTime_at_server1,arrivalTime_at_server2,Server1_available,Server2_available,waitingTime1,servingTime1,servingTime2\n")

#         custm = cust.Customer()
#         Server1_records = pd.read_csv("./data/server1_data.csv")
#         Server2_records = pd.read_csv("./data/server2_data.csv")
#         for i in range(len(Server1_records)):
#             #waiting_queue1.append(Server1_records.loc[i])
#             if wait_time==0:
#                 server1.set_is_busy(False)
#                 server2.set_is_busy(False)
#                 Server1_available=not(server1.is_busy())
#                 Server2_available=not(server2.is_busy())
#             else:
#                 server1.set_is_busy(True)
#                 server2.set_is_busy(True)
#                 Server1_available=not(server1.is_busy())
#                 Server2_available=not(server2.is_busy())


#         # print("waiting queue \n",waiting_queue1)
#             custm.set_call_id(int(Server1_records.loc[i, "call_id"]))
#             custm.set_arrival_time(datetime.datetime.strptime(Server1_records.loc[i, "arrival_time"],format))
#             custm.set_inter_arrival_time(int(Server1_records.loc[i, "interarrival_time"]))
#             custm.set_service_length(int(Server1_records.loc[i, "service_length"]))
#             interval_time_server1 = custm.get_inter_arrival_time()
#             interval_time_server2 = int(Server2_records.loc[i, "interarrival_time"])
#             service_length_server1 = int(Server1_records.loc[i, "service_length"])
#             service_length_server2 = int(Server2_records.loc[i, "service_length"])
#             arrival_time_at_server1=custm.get_arrival_time()
#             custm.set_arrival_time(datetime.datetime.strptime(Server2_records.loc[i, "arrival_time"],format))
#             arrival_time_at_server2=custm.get_arrival_time()

#             if custm.get_call_id() == 1:
#                 wait_time = 0
#             else:
#                 wait_time = service_length_server1+service_length_server2-interval_time_server1
#                 if wait_time < 0:
#                     wait_time = 0
#             totalWaitingTime_at_server1 += wait_time
#             service_time_at_server_1 = service_length_server1
#             service_time_at_server_2 = service_length_server2
#             total_service_time_at_server_1 += service_time_at_server_1
#             total_service_time_at_server_2 += service_time_at_server_2
#             server1_busy_time = service_time_at_server_1+service_time_at_server_2-interval_time_server1
#             if server1_busy_time<0:
#                 server1_busy_time=0
#             server2_busy_time = service_time_at_server_2+service_time_at_server_1-interval_time_server2
#             if server2_busy_time<0:
#                 server2_busy_time=0
#             server1_idle_time = server1_busy_time-service_time_at_server_1
#             server2_idle_time = server2_busy_time-service_time_at_server_2
#             total_server1_idle_time += server1_idle_time
#             total_server2_idle_time += server2_idle_time
#             outRes.write(str(custm.get_call_id())+","+str(interval_time_server1)+","+str(arrival_time_at_server1)+","+str(arrival_time_at_server2)+","+str(Server1_available)+","+str(Server2_available)+","+str(wait_time)+","+str(service_time_at_server_1)+","+str(service_time_at_server_2)+"\n")
#         avg_waiting_time = totalWaitingTime_at_server1//len(Server1_records)
#         avg_service_time_server1 = total_service_time_at_server_1//len(Server1_records)
#         avg_service_time_server2 = total_service_time_at_server_2//len(Server1_records)
#         print("avg_waiting_time,avg_service_time_server1,avg_service_time_server2", avg_waiting_time, avg_service_time_server1, avg_service_time_server2)
#         print("total_server1_idle_time,total_server2_idle_time",total_server1_idle_time,total_server2_idle_time)






# meth=CallCenterSimulation.main()




