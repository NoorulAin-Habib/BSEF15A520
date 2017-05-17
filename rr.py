processes={}
arrival_time=[]
burst_time=[]
remaining_time=[]
flag=0
num=input("Enter Number of processes: ")
quantum_time=input("Enter quantum time: ")
remian=num
for count in range(0,num):
    print "p[",count,"]: "
    a_time=input("Arrival Time:")
    arrival_time.append(a_time)
    b_time=input("Burst Time:")
    burst_time.append(b_time)
    remaining_time[count+1]=burst_time[count+1]
for (time,count,remian) in (0,0,10):
    if(remaining_time[count]<=quantum_time and remain_time[count]>0):
         time+=remaining_time[count]
         remaining_time[count]=0
         flag=1
    elif(remaining_time[count]>0):
         remaining_time[count]-=quantum_time
         time+=quantum+time
    if(remaining_time[count]==0 and flag==1):
         remain=remain-1
         print "p[",i,"]: ", "\t",  arrival_time[i], "\t\t\t" , burst_time[i] ,count+1,time-arrival_timecount, time-arrival_time[count]-burst_time[count]
         waiting_time+=time-arrival_time[count]-burst_time[count]
         turnaround_time+=time-arrival_time[count]
         flag=0
    if(count==num-1):
         count=0
    elif(arrival_time[count+1]<=time):
         count=count+1
    else:
         count=0

