processes={}
burst_time=[]
waiting_time=[]
turnaround_time=[]
priority=[]
arrival_time=0
total=0
num=input("Enter total number of Processes: ")
for i in range (0,num):
   print "P[",i,"]:"
   prio=input("Priority Number: ")
   priority.append(prio)
   b_time=input("Burst Time: ")
   burst_time.append(b_time)
   print ("\n")
   processes[priority[i]] = [i+1 , arrival_time , burst_time[i]]

priority.sort()

total = processes.get(priority[0])[1]
min = total
if(total>0):
	print '0 -------' , total 

for i in range (0,num):
	total = total + processes.get(priority[i])[2]
	print min , "________" , total
	min = total
for i in range (0,num):
	total = total + processes.get(priority[i])[0]
        var=processes.get(priority[i])[1]
        wt_time=min
        ta_time=total
        waiting_time.insert(var,wt_time)
        turnaround_time.insert(var,ta_time)
print   "Process         Arrival Time           Burst Time"
for i in range (0,num):
	print "p[",i,"]: ", "\t",  arrival_time, "\t\t\t" , burst_time[i]
print   "Process        Waiting Time           TurnAround Time"
for i in range (0,num):
        print  "p[",i,"]: ",  "\t\t"  ,  waiting_time[i] ,"\t\t\t" , turnaround_time[i]

