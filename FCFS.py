total = 0
processes={}
burst_time=[]
arrival_time=[]
waiting_time=[]
turnaround_time=[]
n = input("Enter the number of processes:")
for i in range (0,n):
        print "p[",i+1,"]: "
	a_time=input("Arrival Time:")
	arrival_time.append(a_time)
	b_time=input("Burst Time:")
	burst_time.append(b_time)
	processes[arrival_time[i]] = [arrival_time[i], burst_time[i]]

print "Process     Arrival Time           Burst Time"
for i in range (0,n):
	print "p[",i+1,"]: ", "\t",  arrival_time[i], "\t\t\t" , burst_time[i]
arrival_time.sort()
total = processes.get(arrival_time[0])[0]
min = total
if(total>0):
	print '0 -------' , total 

for i in range (0,n):
	total = total + processes.get(arrival_time[i])[1]
        ind=processes.get(arrival_time[i])[0]
        arr_time=arrival_time[i]
        w_time=min-arr_time
        t_time=total-arr_time
        waiting_time.insert(ind,w_time)
        turnaround_time.insert(ind,t_time)
	print min , "________" , total
	min = total
print   "Process        Waiting Time           TurnAround Time"
for i in range (0,n):
        print  "p[",i+1,"]: ",  "\t\t"  ,  waiting_time[i] ,"\t\t\t" , turnaround_time[i]

