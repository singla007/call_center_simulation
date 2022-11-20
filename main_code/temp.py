import sys
import pandas as pd
import datetime
import Customer as cust
import server1 as serv


def call_centre():
    # Intializing servers
    server1 = serv.Server()
    server2 = serv.Server()
    server3 = serv.Server()
    server4 = serv.Server()

    waiting_queue1 = list()
    waiting_queue2 = list()
    record = ""
    total_server1_service_time = 0
    total_server2_service_time = 0
    total_server3_service_time = -1
    total_server4_service_time = -1
    Server1_available = False
    Server2_available = False
    total_wait_time = 0

    # Getting data
    from_data = 5
    upto_data = 55
    server1_data = pd.read_csv("./processed_data/server1_data.csv").iloc[from_data:upto_data]
    server2_data = pd.read_csv("./processed_data/server2_data.csv").iloc[from_data:upto_data]
    server3_data = pd.read_csv("./processed_data/server3_data.csv").iloc[from_data:upto_data]
    server4_data = pd.read_csv("./processed_data/server4_data.csv").iloc[from_data:upto_data]
    server1_service_time = list(server1_data['service_length'])
    server2_service_time = list(server2_data['service_length'])
    server3_service_time = list(server3_data['service_length'])
    server4_service_time = list(server4_data['service_length'])
    server_chosen = list(server2_data['server_chosen'])
    customer_interarrival_time = list(server1_data['interarrival_time'])
    customer_arrival_time = list()

    # Create arrival time with respect to 0
    current_arrival_time = 0
    for i in customer_interarrival_time:
        current_arrival_time += i
        customer_arrival_time.append(current_arrival_time)

    # Intializing all the indexs
    customer_index = 0
    service_index1 = 0
    service_index2 = 0
    service_index3 = 0
    service_index4 = 0
    server_chosen_index = 0
    custom_timer = 0
    customer_index_queue2 = 0
    max_queue1_length = 0
    max_queue2_length = 0
    print(customer_arrival_time)

    queue1_wait_time = 0
    queue2_wait_time = 0
    customers_waited_in_queue1 = 0
    customers_waited_in_queue2 = 0



    while True:
        if custom_timer == 15:
            print("Start")
        print("custom_timer", custom_timer)

        queue1_wait_time += len(waiting_queue1)
        queue2_wait_time += len(waiting_queue2)
        # Customer arrival
        if custom_timer >= customer_arrival_time[customer_index]:
            waiting_queue1.append(customer_index)
            customer_index += 1

        # Customer entering into server 2
        if (server1.curr_service_end + 1) == custom_timer and custom_timer!=0:
            print("Inside server 2")
            server2.curr_service_begin = custom_timer
            server2.curr_service_end = custom_timer + server2_service_time[service_index2]
            service_index2 += 1
            server2.is_busy = True
            server1.curr_service_begin = -1
            server1.curr_service_end = -1

        # Customer entering into server 1
        if not server1.is_busy and not server2.is_busy and len(waiting_queue1) >= 1:
            print("Inside server 1")
            server1.curr_service_begin = custom_timer
            server1.curr_service_end = custom_timer + server1_service_time[service_index1]
            service_index1 += 1
            server1.is_busy = True
            waiting_queue1.pop(0)

        # Departure from server 1
        if server1.curr_service_end == custom_timer:
            print("Service 1 end")
            server1.is_busy = False
            server1.total_server_busy_time += server1.curr_service_end - server1.curr_service_begin

        # Departure from server 2
        if server2.curr_service_end == custom_timer:
            print("Service 2 end")
            server2.is_busy = False
            server2.total_server_busy_time += server2.curr_service_end - server2.curr_service_begin
            server2.curr_service_begin = -1
            server2.curr_service_end = -1
            waiting_queue2.append(server_chosen[server_chosen_index])
            server_chosen_index +=1

        # Customer entering into server 3 and 4
        if len(waiting_queue2) >=1:
            if len(waiting_queue2)>=1 and waiting_queue2[0] == "S3" and not server3.is_busy:
                print("Inside server 3")
                server3.is_busy = True
                server3.curr_service_begin = custom_timer
                server3.curr_service_end = custom_timer + server3_service_time[service_index3]
                service_index3 += 1
                waiting_queue2.pop(0)

            if len(waiting_queue2)>=1 and waiting_queue2[0] == "S4" and not server4.is_busy:
                print("Inside server 4")
                server4.is_busy = True
                server4.curr_service_begin = custom_timer
                server4.curr_service_end = custom_timer + server4_service_time[service_index4]
                service_index4 += 1
                waiting_queue2.pop(0)

        # Departure from server 3
        if server3.curr_service_end == custom_timer:
            server3.total_server_busy_time += server3.curr_service_end - server3.curr_service_begin
            server3.is_busy = False
            server3.curr_service_begin = -1
            server3.curr_service_end = -1

        # Departure from server 4
        if server4.curr_service_end == custom_timer:
            server4.total_server_busy_time += server4.curr_service_end - server4.curr_service_begin
            server4.is_busy = False
            server4.curr_service_begin = -1
            server4.curr_service_end = -1

        # Exit conditions
        if customer_index >= server1_data.shape[0] and len(waiting_queue1) == 0 and len(
                waiting_queue2) == 0 and not server1.is_busy and not server2.is_busy and not server3.is_busy and not server4.is_busy:
            break

        if max_queue1_length < len(waiting_queue1):
            max_queue1_length = len(waiting_queue1)

        if max_queue2_length < len(waiting_queue2):
            max_queue2_length = len(waiting_queue2)

        custom_timer += 1
        simulation_run_length = custom_timer

        print("waiting_queue1", waiting_queue1)
        print("total_server1_service_time", server1.total_server_busy_time)
        print("total_server2_service_time", server2.total_server_busy_time)
        print("total_server3_service_time", server3.total_server_busy_time)
        print("total_server4_service_time", server4.total_server_busy_time)
        print("total simulation time", )
        print("waiting_queue2", waiting_queue2)
        print("Max queue 1 length", max_queue1_length)
        print("Max queue 2 length", max_queue2_length)
        print("Idle server1 time", simulation_run_length -  server1.total_server_busy_time)
        print("Idle server2 time", simulation_run_length - server2.total_server_busy_time)
        print("Idle server3 time", simulation_run_length - server3.total_server_busy_time)
        print("Idle server4 time", simulation_run_length - server4.total_server_busy_time)
        print("Mean Interarrival time", sum(customer_interarrival_time)/len(customer_interarrival_time))
        print("Mean service time for server 1", sum(server1_service_time)/len(server1_service_time))
        print("Mean service time for server 2", sum(server2_service_time) / len(server2_service_time))
        print("Mean service time for server 3", sum(server3_service_time) / len(server3_service_time))
        print("Mean service time for server 4", sum(server4_service_time) / len(server4_service_time))


call_centre()