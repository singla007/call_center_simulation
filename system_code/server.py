class server:
    def __init__(self):
        self.is_busy = False
        self.curr_service_time = None
        self.is_fail = False
        self.server_recovery_time = 5
        self.curr_service_begin = 0
        self.curr_service_end_at = None
        self.total_server_busy_time = 0