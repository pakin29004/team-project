from team01 import*

print("=====Process Scheduling=====")
print("Please Choose CPU scheduling technique")
print("1.Non-Preemptive Scheduling\n2.Preemptive Scheduling ")
choose_algorithm = int(input("Choose Scheduling (1/2): "))
if choose_algorithm ==1 :
    print("Non-Preemptive Scheduling")
    print("====Process Scheduling Algorithms=====")
    print("1.First Come Fist Serve(FCFS) \n2.Shortest Job First(SJF)\n3.Priority(PR)")
    choose_process = str(input("Please Choose Process Scheduling : "))
    if choose_process == 'fcfs' :
        num_process = int(input("Number of process : "))
        d = dict()
        for i in range(num_process) :
            Process = str(i+1)
            print("P",Process," : ")
            arrivalTime_ = int(input(f"Arrival Time [{i}]: "))
            busrtTime_ = int(input(f"Burst Time of [{i}]: "))
            list_ = []
            list_.append(arrivalTime_)
            list_.append(busrtTime_)
            #l.append(priority_values)
            d[Process] = list_
        d = sorted(d.items(), key=lambda items: items[1][0])
        completion_ = []
        for i in range(len(d)):
                # first process
                if(i==0):
                    completion_.append(d[i][1][1])
 
                # get prevET + newBT
                else:
                    completion_.append(completion_[i-1] + d[i][1][1])
 
        tAround = []
        for i in range(len(d)):
            tAround.append(completion_[i] - d[i][1][0])
 
        waiting = []
        for i in range(len(d)):
            waiting.append(tAround[i] - d[i][1][1])
 
        avg_WT = 0
        for i in waiting:
            avg_WT +=i
        avg_WT = (avg_WT/num_process)
        
        avg_TT = 0
        for i in tAround:
            avg_TT +=i
        avg_TT = (avg_TT/num_process)

        print("Process | Arrival | Burst Time | Completion Time | Turnaround Time| Waiting Time |")
        for i in range(num_process):
            print("P",d[i][0],"       ",d[i][1][0],"          ",d[i][1][1],"            ",completion_[i],"             ",tAround[i],"             ",waiting[i],"   ")
        print(f"Average Waiting Time: {avg_WT:.2f}")
        print(f"Average Turnaround Time: {avg_TT:.2f}")

    # if choose_process == 'sjf':
    #     class SJF:
    #         def processData(self, num_process_ID):
    #             process_data = []
    #             for i in range(num_process_ID):
    #                 temporary = []
    #                 process_id = int(input("Enter Process ID: "))
    #                 arrivalTime_values = int(input(f"Arrival Time of Process[{process_id}]: "))
    #                 busrtTime_values = int(input(f"Burst Time of Process[{process_id}]: "))
    #                 print("")

    #                 temporary.extend([process_id, arrivalTime_values, busrtTime_values, 0]) 
                    
    #                 process_data.append(temporary)
    #             SJF.schedulingProcess(self, process_data)

    #         def schedulingProcess(self, process_data):
    #             start_time = []
    #             exit_time = []
    #             s_time = 0
    #             process_data.sort(key=lambda x: x[1])
                
    #             for i in range(len(process_data)):
    #                 ready_queue = []
    #                 temp = []
    #                 normal_queue = []

    #                 for j in range(len(process_data)):
    #                     if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
    #                         temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
    #                         ready_queue.append(temp)
    #                         temp = []
    #                     elif process_data[j][3] == 0:
    #                         temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
    #                         normal_queue.append(temp)
    #                         temp = []

    #                 if len(ready_queue) != 0:
    #                     ready_queue.sort(key=lambda x: x[2])
                        
    #                     start_time.append(s_time)
    #                     s_time = s_time + ready_queue[0][2]
    #                     e_time = s_time
    #                     exit_time.append(e_time)
    #                     for k in range(len(process_data)):
    #                         if process_data[k][0] == ready_queue[0][0]:
    #                             break
    #                     process_data[k][3] = 1
    #                     process_data[k].append(e_time)

    #                 elif len(ready_queue) == 0:
    #                     if s_time < normal_queue[0][1]:
    #                         s_time = normal_queue[0][1]
    #                     start_time.append(s_time)
    #                     s_time = s_time + normal_queue[0][2]
    #                     e_time = s_time
    #                     exit_time.append(e_time)
    #                     for k in range(len(process_data)):
    #                         if process_data[k][0] == normal_queue[0][0]:
    #                             break
    #                     process_data[k][3] = 1
    #                     process_data[k].append(e_time)

    #             t_time = SJF.calculateTurnaroundTime(self, process_data)
    #             w_time = SJF.calculateWaitingTime(self, process_data)
    #             SJF.printData(self, process_data, t_time, w_time)


    #         def calculateTurnaroundTime(self, process_data):
    #             total_turnaround_time = 0
    #             for i in range(len(process_data)):
    #                 turnaround_time = process_data[i][4] - process_data[i][1]
                    
    #                 total_turnaround_time = total_turnaround_time + turnaround_time
    #                 process_data[i].append(turnaround_time)
    #             average_turnaround_time = total_turnaround_time / len(process_data)
                
    #             return average_turnaround_time


    #         def calculateWaitingTime(self, process_data):
    #             total_waiting_time = 0
    #             for i in range(len(process_data)):
    #                 waiting_time = process_data[i][5] - process_data[i][2]
                    
    #                 total_waiting_time = total_waiting_time + waiting_time
    #                 process_data[i].append(waiting_time)
    #             average_waiting_time = total_waiting_time / len(process_data)
                
    #             return average_waiting_time


    #         def printData(self, process_data, average_turnaround_time, average_waiting_time):
    #             process_data.sort(key=lambda x: x[0])
                
    #             print("Process |    Arrival  |    Burst Time  |  Completed  |  Completion Time | Turnaround Time |  Waiting Time |")

    #             for i in range(len(process_data)):
    #                 for j in range(len(process_data[i])):
                        
    #                     print(process_data[i][j], end="\t\t")
    #                 print()

    #             print(f'Average Waiting Time: {average_waiting_time:.2f}')
    #             print("")
    #             print("ในหัวข้อ Completed ถ้าค่าเป็น 0 แสดงว่า executed ไม่สำเร็จ แต่ถ้าค่าเป็น 1 แสดงว่า execution สำเร็จแล้ว")


    #     if __name__ == "__main__":
    #         num_process_ID = int(input("No of Process [1-10]: "))
    #         print("")
    #         while num_process_ID < 1:
    #             print("Try Again")
    #             num_process_ID = int(input("No of Process [1-10]: "))
    #             print("")
    #         while num_process_ID > 10:
    #             print("Try Again")
    #             num_process_ID = int(input("No of Process [1-10]: "))
    #             print("")
    #         sjf = SJF()
    #         sjf.processData(num_process_ID)
   
   
    else :
        print("Please Choose Process(fcfs/sjf/pr)")       
if choose_algorithm == 2 :
    print("Hi")

