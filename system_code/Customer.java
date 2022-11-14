/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package call_center_simulation;

import java.util.Date;

/**
 *
 * @author Jack Napier
 */
public class Customer {
    private int callId;
    private Date arrivalTime;
    private int interArrivalTime;
    private int serviceLength;
    private int waitingTime1 = 0;
    private int servingTime1 = 0;
    private int waitingTime2 = 0;
    private int servingTime2 = 0;


    public int getCallId() {
        return callId;
    }

    public void setCallId(int callId) {
        this.callId = callId;
    }

    public Date getArrivalTime() {
        return arrivalTime;
    }

    public void setArrivalTime(Date arrivalTime) {
        this.arrivalTime = arrivalTime;
    }
    

    public int getInterArrivalTime() {
        return interArrivalTime;
    }

    public void setInterArrivalTime(int interArrivalTime) {
        this.interArrivalTime = interArrivalTime;
    }

    public int getServiceLength() {
        return serviceLength;
    }

    public void setServiceLength(int serviceLength) {
        this.serviceLength = serviceLength;
    }
    
    public int getWaitingTime1() {
        return waitingTime1;
    }

    public void setWaitingTime1(int waitingTime1) {
        this.waitingTime1 = waitingTime1;
    }

    public int getServingTime1() {
        return servingTime1;
    }

    public void setServingTime1(int servingTime1) {
        this.servingTime1 = servingTime1;
    }

    public int getWaitingTime2() {
        return waitingTime2;
    }

    public void setWaitingTime2(int waitingTime2) {
        this.waitingTime2 = waitingTime2;
    }

    public int getServingTime2() {
        return servingTime2;
    }

    public void setServingTime2(int servingTime2) {
        this.servingTime2 = servingTime2;
    }
}
