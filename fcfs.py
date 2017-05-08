processes={}
arrival_time=[]
burst_time=[]
waiting_time=[]
turnaround_time=[]
total_time=0
num=input("Enter Total number of processes: ")
for i in range(0,num):
  print "p[",i,"]: "
  al_time=input("Arrival Time: ")
  arrival_time.append(al_time)
  bt_time=input("Burst Time: ")
  burst_time.append(bt_time)
  processes[arrival_time[i]] = [arrival_time[i], burst_time[i]]
arrival_time.sort()
total = processes.get(arrival_time[0])[0]
min = total 
print "\nCPU is remain idle in time"
print "0......." , total
print "Process"
for i in range (0,num):
	print "p[",i,"]: "
	total = total + burst_time[i]
        print min , "________" , total
	min = total
for i in range (0,num):
	total = total + processes.get(arrival_time[i])[1]
        var=processes.get(arrival_time[i])[0]
        arr_time=arrival_time[i]
        wt_time=min-arr_time
        ta_time=total-arr_time
        waiting_time.insert(var,wt_time)
        turnaround_time.insert(var,ta_time)
print   "Process         Arrival Time           Burst Time"
for i in range (0,num):
	print "p[",i,"]: ", "\t",  arrival_time[i], "\t\t\t" , burst_time[i]
print   "Process        Waiting Time           TurnAround Time"
for i in range (0,num):
        print  "p[",i,"]: ",  "\t\t"  ,  waiting_time[i] ,"\t\t\t" , turnaround_time[i]

