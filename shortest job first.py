
processes={}
burst_time=[]
arrival_time=0
waiting_time=[]
turnaround_time=[]
total=0
num = input("Enter the number of processes:")
for i in range (0,num):
        print "p[",i,"]: "
	b_time=input("Burst Time:")
	burst_time.append(b_time)
	processes[burst_time[i]] = [i+1 , arrival_time]

print "Process       Arrival Time           Burst Time"
burst_time.sort()
total = processes.get(burst_time[0])[1]
min = total
if(total>0):
	print '0 -------' , total 

for i in range (0,num):
	total = total + burst_time[i]
	print min , "________" , total
	min = total
for i in range (0,num):
	total = total + processes.get(burst_time[i])[0]
        var=processes.get(burst_time[i])[0]
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
