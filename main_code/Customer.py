from datetime import date,time
class Customer:
    def __init__(self):
        self.__servingTime2 = 0
        self.__waiting_time2 = 0
        self.__serving_time1 = 0
        self.__waiting_time1 = 0
        self.__service_length = 0
        self.__inter_arrival_time = 0
        self.__arrivalTime = date.today
        self.__callId =0

    def get_call_id(self):
        return self.__callId

    def set_call_id(self, call_id):
        self.__callId = call_id

    def get_arrival_time(self):
        return self.__arrivalTime

    def set_arrival_time(self,arrival_time):
        self.__arrivalTime = arrival_time

    def get_inter_arrival_time(self):
        return self.__inter_arrival_time

    def set_inter_arrival_time(self,inter_arrival_time):
        self.__inter_arrival_time = inter_arrival_time

    # def get_service_length(self):
    #     return self.__service_length

    # def set_service_length(self, service_length):
    #     self.__service_length = service_length

    def get_waiting_time(self):
        return self.waiting_time1

    def set_waiting_time(self, waiting_time1):
        self.__waiting_time1 = waiting_time1

    # def get_serving_time1(self):
    #     return self.__serving_time1

    # def set_serving_time1(self, serving_time1):
    #     self.__serving_time1 = serving_time1

    # def get_waiting_time2(self):
    #     return self.__waiting_time2

    # def set_waiting_time2(self, waiting_time2):
    #     self.__waiting_time2 = waiting_time2;

    # def get_serving_time2(self):
    #     return self.__serving_time2;

    # def set_serving_time2(self, serving_time2):
    #     self.__servingTime2 = serving_time2

