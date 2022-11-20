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
    total_server1_idle_time = 0
    total_server2_idle_time = 0
    total_server3_service_time = 0
    total_server4_service_time = 0
    Server1_available = False
    Server2_available = False
    total_wait_time = 0

    # Getting data
    server1_data = pd.read_csv("./processed_data/server1_data.csv").iloc[:10]
    server2_data = pd.read_csv("./processed_data/server2_data.csv").iloc[:10]
    server3_data = pd.read_csv("./processed_data/server3_data.csv").iloc[:10]
    server4_data = pd.read_csv("./processed_data/server4_data.csv").iloc[:10]
    server1_service_time = list(server1_data['service_length'])
    server2_service_time = list(server2_data['service_length'])
    server3_service_time = list(server3_data['service_length'])
    server4_service_time = list(server4_data['service_length'])
    print(server2_data)
    server_chosen = list(server2_data['server_chosen'])
    customer_interarrival_time = list(server1_data['interarrival_time'])
    customer_arrival_time = list()

    # Create arrival time with respect to 0
    current_arrival_time = 0
    customer_arrival_time.append(current_arrival_time)
    for i in customer_interarrival_time:
        current_arrival_time += i
        customer_arrival_time.append(i)

    # Intializing all the indexs
    customer_index = 0
    service_index12 = 0
    service_index3 = 0
    service_index4 = 0
    custom_timer = 0
    customer_index_queue2 = 0
    max_queue_length = 0

    while True:
        # Adding current wait time
        total_wait_time += len(waiting_queue1)

        # Customer arrival
        if custom_timer >= customer_arrival_time[customer_index]:
            waiting_queue1.append(customer_index)
            customer_index += 1
        
        # Sending customers for service
        if not server1.is_busy and not server2.is_busy and len(waiting_queue1):
            server1.set_next_service_available_at = custom_timer + server1_service_time[service_index12] + server2_service_time[service_index12]
            server2.set_next_service_available_at = custom_timer + server1_service_time[service_index12] + server2_service_time[service_index12]
            total_server1_idle_time = server2_service_time[service_index12]
            total_server2_idle_time = server1_service_time[service_index12]
            waiting_queue1.pop(0)
            service_index12 += 1
        
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

        # Checking status of server1
        if server1.get_next_service_available_at() == custom_timer:
            server1.is_busy = False

        
        # Checking status of server2
        if server2.get_next_service_available_at() == custom_timer:
            server2.is_busy = False

        # Checking max queue1 length
        if max_queue_length < len(waiting_queue1):
            max_queue_length = len(waiting_queue1)
        
        # Exit conditions
        if customer_index >= server1_data.shape[0] and len(waiting_queue1)==0 and len(waiting_queue2)==0 and not server1.is_busy and not server2.is_busy and not server3.is_busy and not server4.is_busy:
            break
        
        custom_timer += 1 
        print(waiting_queue1)
        print(total_server1_idle_time)
        print(total_server2_idle_time)


call_centre()