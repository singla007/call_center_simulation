class Server:

    def __init__(self):
        self.is_busy = False
        self.curr_service_time = 0
        self.is_fail = 0
        self.server_recovery_time = 5
        self.curr_service_begin = -1
        self.curr_service_end = -1
        self.total_server_busy_time = 0

