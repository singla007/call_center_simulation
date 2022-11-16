/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package call_center_simulation;

/**
 *
 * @author Jack Napier
 */
public class Server {
    
    private boolean is_busy = false;
    private int curr_service_time = 0;
    private boolean is_fail = false;
    private final int server_recovery_time = 5;
    private int curr_service_begin = 0;
    private int curr_service_end_at = 0;
    private int total_server_busy_time = 0;
    
    
    public boolean isIs_busy() {
        return is_busy;
    }

    public void setIs_busy(boolean is_busy) {
        this.is_busy = is_busy;
    }

    public int getCurr_service_time() {
        return curr_service_time;
    }

    public void setCurr_service_time(int curr_service_time) {
        this.curr_service_time = curr_service_time;
    }

    public boolean isIs_fail() {
        return is_fail;
    }

    public void setIs_fail(boolean is_fail) {
        this.is_fail = is_fail;
    }
    
    public int getServer_recovery_time() {
        return server_recovery_time;
    }

    public int getCurr_service_begin() {
        return curr_service_begin;
    }

    public void setCurr_service_begin(int curr_service_begin) {
        this.curr_service_begin = curr_service_begin;
    }

    public int getCurr_service_end_at() {
        return curr_service_end_at;
    }

    public void setCurr_service_end_at(int curr_service_end_at) {
        this.curr_service_end_at = curr_service_end_at;
    }

    public int getTotal_server_busy_time() {
        return total_server_busy_time;
    }

    public void setTotal_server_busy_time(int total_server_busy_time) {
        this.total_server_busy_time = total_server_busy_time;
    }
}
