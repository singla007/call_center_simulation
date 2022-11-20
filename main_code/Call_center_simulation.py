import sys
import pandas as pd
import datetime
import Customer as cust
import Server as serv


def call_centre():
    # Intializing servers
    server1 = serv.Server()
    server2 = serv.Server()
    server3 = serv.Server()
    server4 = serv.Server()

    waiting_queue1 = list()
    waiting_queue2 = list()
    record = ""
    total_server1_service_time = -1
    total_server2_service_time = 0
    total_server3_service_time = -1
    total_server4_service_time = -1
    Server1_available = False
    Server2_available = False
    total_wait_time = 0

    # Getting data
    upto_data = 50
    server1_data = pd.read_csv("./processed_data/server1_data.csv").iloc[:upto_data]
    server2_data = pd.read_csv("./processed_data/server2_data.csv").iloc[:upto_data]
    server3_data = pd.read_csv("./processed_data/server3_data.csv").iloc[:upto_data]
    server4_data = pd.read_csv("./processed_data/server4_data.csv").iloc[:upto_data]
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
    service_index12 = 0
    service_index3 = 0
    service_index4 = 0
    custom_timer = 0
    customer_index_queue2 = 0
    max_queue1_length = 0
    max_queue2_length = 0
    print(customer_arrival_time)
    while True:
        print("custom_timer", custom_timer)
        # Adding current wait time
        total_wait_time += len(waiting_queue1)

        # Customer arrival
        if custom_timer >= customer_arrival_time[customer_index]:
            waiting_queue1.append(customer_index)
            customer_index += 1

        # Checking status of server1
        if server2.curr_service_begin == custom_timer:
            server1.is_busy = False
            server2.is_busy = True

        # Checking status of server2
        if server2.get_next_service_available_at() == custom_timer:
            server2.is_busy = False
            waiting_queue2.append(server_chosen[customer_index_queue2])
            customer_index_queue2 += 1

        # Checking status of server3
        if server3.get_next_service_available_at() == custom_timer:
            server3.is_busy = False

        # Checking status of server4
        if server4.get_next_service_available_at() == custom_timer:
            server4.is_busy = False
        
        # Sending customers for service
        # print(server2.is_busy, server1.is_busy)
        if not server1.is_busy and not server2.is_busy and len(waiting_queue1)>=1:
            server1.next_service_available_at = custom_timer + server1_service_time[service_index12] + server2_service_time[service_index12]
            server2.next_service_available_at = custom_timer + server1_service_time[service_index12] + server2_service_time[service_index12]
            server1.is_busy = True
            server1.curr_service_end = custom_timer + server1_service_time[service_index12]
            server2.curr_service_begin = server1.curr_service_end
            # total_server1_idle_time += server2_service_time[service_index12]
            # total_server2_idle_time += server1_service_time[service_index12]
            waiting_queue1.pop(0)
            service_index12 += 1

        if server1.is_busy:
            total_server1_service_time += 1

        if server2.is_busy:
            total_server2_service_time += 1

        if not server3.is_busy and len(waiting_queue2) and waiting_queue2[-1] == 'S3':
            server3.set_next_service_available_at = custom_timer + server3_service_time[service_index3] 
            total_server3_service_time += server3_service_time[service_index3] 
            waiting_queue2.pop(0)
            service_index3 += 1

        if not server4.is_busy and len(waiting_queue2) and waiting_queue2[-1] == 'S4':
            server4.set_next_service_available_at = custom_timer + server4_service_time[service_index4] 
            total_server4_service_time += server4_service_time[service_index4] 
            waiting_queue2.pop(0)
            service_index4 += 1
        




        # Checking max queue1 length
        if max_queue1_length < len(waiting_queue1):
            max_queue1_length = len(waiting_queue1)
        
        if max_queue2_length < len(waiting_queue2):
            max_queue2_length = len(waiting_queue2)

        # Exit conditions
        if customer_index >= server1_data.shape[0] and len(waiting_queue1)==0 and len(waiting_queue2)==0 and not server1.is_busy and not server2.is_busy and not server3.is_busy and not server4.is_busy:
            break
        
        custom_timer += 1 
        print("waiting_queue1", waiting_queue1)
        print("total_server1_service_time", total_server1_service_time)
        print("total_server2_service_time", total_server2_service_time)
        print("total_server3_service_time", total_server3_service_time)
        print("total_server4_service_time", total_server4_service_time)
        print("waiting_queue2", waiting_queue2)
    print("Max queue 1 length", max_queue1_length)
    print("Max queue 2 length", max_queue2_length)


call_centre()