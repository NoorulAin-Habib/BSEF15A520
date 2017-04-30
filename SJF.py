
total = 0
processes={}
burst_time=[]
arrival_time=0
n = input("Enter the number of processes:")
for i in range (0,n):
        print "p[",i+1,"]: "
	b_time=input("Burst Time:")
	burst_time.append(b_time)
	processes[burst_time[i]] = [i+1 , arrival_time]

print "Process       Arrival Time           Burst Time"
for i in range (0,n):
	print "p[",i+1,"]","\t\t ", arrival_time, "\t\t\t" , burst_time[i] 

burst_time.sort()
total = processes.get(burst_time[0])[1]
min = total
if(total>0):
	print '0 -------' , total 

for i in range (0,n):
	total = total + burst_time[i]
	print min , "________" , total
	min = total

