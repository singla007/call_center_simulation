class Server:

    def __init__(self):
        self.__is_busy= False
        self.__curr_service_time=0
        self.__is_fail=0
        self.__server_recovery_time=5
        self.__curr_service_begin = 0
        self.__next_service_available_at=0
        self.__total_server_busy_time=0

    def is_busy(self):
        return self.__is_busy

    def set_is_busy(self, is_busy):
            self.__is_busy = is_busy

    def get_curr_service_time(self):
        return self.__curr_service_time

    def set_curr_service_time(self, curr_service_time):
        self.__curr_service_time = curr_service_time

    def is_is_fail(self):
        return self.__is_fail

    def set_is_fail(self, is_fail):
        self.__is_fail = is_fail

    def get_server_recovery_time(self):
        self.__server_recovery_time

    def get_curr_service_begin(self):
        return self.__curr_service_begin

    def set_curr_service_begin(self, curr_service_begin):
        self.__curr_service_begin = curr_service_begin

    def get_next_service_available_at(self):
        return self.__next_service_available_at

    def set_next_service_available_at(self, next_service_available_at):
        self.__next_service_available_at = next_service_available_at

    def get_total_server_busy_time(self):
        return self.__total_server_busy_time

    def set_total_server_busy_time(self, total_server_busy_time):
        self.__total_server_busy_time = total_server_busy_time

