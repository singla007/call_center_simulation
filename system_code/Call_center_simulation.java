/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package call_center_simulation;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Locale;

/**
 *
 * @author Jack Napier
 */
public class Call_center_simulation {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException, ParseException {

        Server server1 = new Server();
        Server server2 = new Server();

        DateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm", Locale.ENGLISH);

        String record = "";
        int lastServingTime = 0;
        int serverBusyTime = 0;
        int waitingTime = 0;
        int totalWaitingTime = 0;
        BufferedWriter outServ = new BufferedWriter(new FileWriter("src\\call_center_simulation\\data\\results\\serverDataResults.csv", true));
        BufferedWriter outCust = new BufferedWriter(new FileWriter("src\\call_center_simulation\\data\\results\\custDataResults.csv", true));
        outServ.write("serverName,busyTime\n");
        outCust.write("customerId,arrivalTime,waitingTime1,waitingTime2,servingTime1,servingTime2\n");

        try {
            BufferedReader csvReader = new BufferedReader(new FileReader("src\\call_center_simulation\\data\\server1_data.csv"));
            record = csvReader.readLine();
            while ((record = csvReader.readLine()) != null) {
                String[] data1 = record.split(",");

                Customer cust = new Customer();
                cust.setCallId(Integer.parseInt(data1[0]));
                cust.setArrivalTime(df.parse(data1[2]));
                cust.setInterArrivalTime(Integer.parseInt(data1[3]));
                cust.setServiceLength(Integer.parseInt(data1[1]));

                server1.setIs_busy(true);
                server2.setIs_busy(true);
                
                waitingTime = (lastServingTime - cust.getInterArrivalTime()) < 0 ? 0 : (lastServingTime - cust.getInterArrivalTime());

                cust.setWaitingTime1(waitingTime);
                cust.setWaitingTime2(waitingTime);
                cust.setServingTime1(1);
                cust.setServingTime2(cust.getServiceLength());
                serverBusyTime += cust.getServiceLength();
                totalWaitingTime += cust.getWaitingTime1();
                lastServingTime = (lastServingTime - cust.getInterArrivalTime()) + cust.getServiceLength();
                
                if (lastServingTime < 0) {
                    lastServingTime = cust.getServiceLength();
                }

//                if (lastServingTime <= cust.getInterArrivalTime()) {
//                    lastInterArrivalTime += cust.getInterArrivalTime();
//                    lastServingTime += cust.getInterArrivalTime();
//                    cust.setWaitingTime1(lastServingTime - lastInterArrivalTime);
//                    cust.setWaitingTime2(lastServingTime - lastInterArrivalTime);
//                    cust.setServingTime1(1);
//                    cust.setServingTime2(cust.getServiceLength());
//                    serverBusyTime += cust.getServiceLength();
//
//                    lastWaitingTime = (lastWaitingTime - cust.getInterArrivalTime()) + lastServingTime;
//                    lastServingTime = cust.getServiceLength();
//                } else {
//                    lastWaitingTime = (lastWaitingTime - cust.getInterArrivalTime()) + lastServingTime;
//
//                    cust.setWaitingTime1(lastWaitingTime);
//                    cust.setWaitingTime2(lastWaitingTime);
//                    cust.setServingTime1(1);
//                    cust.setServingTime2(cust.getServiceLength());
//                    serverBusyTime += cust.getServiceLength();
//
//                    totalWaitingTime += lastWaitingTime;
//                    lastServingTime = cust.getServiceLength();
//                }

                outCust.write(cust.getCallId() + "," + cust.getArrivalTime() + "," + cust.getWaitingTime1() + "," + cust.getWaitingTime2() + "," + cust.getServingTime1() + "," + cust.getServingTime2() + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        outServ.write("seever1," + serverBusyTime + "\n");
        outServ.write("seever2," + serverBusyTime + "\n");

        outServ.close();
        outCust.close();

        System.out.println("Total Serving Time : " + serverBusyTime);
        System.out.println("Total waiting Time : " + totalWaitingTime);

        server1.setIs_busy(false);
        server2.setIs_busy(false);
    }

}
