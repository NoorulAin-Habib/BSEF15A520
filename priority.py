#!usr/bin/env python


total = 0
priority=[]
processes={}
burst_time=[]
arrival_time=0
n = input("Enter the number of processes:")
for i in range (0,n):
        print "p[",i+1,"]: "
	prio_no=input("Priority number:")
	priority.append(prio_no)
	b_time=input("Burst Time:")
	burst_time.append(b_time)
	processes[priority[i]] = [i+1 , arrival_time , burst_time[i]]

print "Process    Priority_No           Arrival Time             Burst Time"
for i in range (0,n):
	print "p[",i+1,"]","\t\t",  priority[i] , "\t\t\t" , arrival_time, "\t\t\t" , burst_time[i] 

priority.sort()

total = processes.get(priority[0])[1]
min = total
if(total>0):
	print '0 -------' , total 

for i in range (0,n):
	total = total + processes.get(priority[i])[2]
	print min , "________" , total
	min = total

