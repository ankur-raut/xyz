n = int(input('Enter no of processes: '))
bt = [0] * (n + 1)
at = [0] * (n + 1)
abt = [0] * (n + 1)
temp=[0] * (n + 1)
for i in range(n):
  abt[i] = int(input('Enter the burst time for process {} : '.format(i + 1)))
  at[i] = int(input('Enter the arrival time for process {} : '.format(i + 1))) 
  temp[i]=abt[i]
time_quantum=int(input("Enter the Time Quantum"))
total=0 #stores the completion time
i=0 #Counter Variable
counter= 0 #Boolean Value checks if process is i=over or not
x=n #number of processes
limit=x
while(x!=0):
  if (temp[i] <= time_quantum and temp[i] > 0): # burst time is about to get over
    total = total + temp[i]
    temp[i] = 0
    counter = 1
  elif(temp[i] > 0): # if burst time is not getting over 
    temp[i] = temp[i] - time_quantum;
    total = total + time_quantum;
  if(temp[i] == 0 and counter == 1):
        x=x-1 #One Process Down
        turn_ard_time= total - at[i]
        wait_time= turn_ard_time - abt[i]
        print("Process ", i+1,end=" ")
        print(" Completion Time ", total,end=" ")
        print(" Burst Time ", abt[i],end=" ")
        print(" Turn Around Time ", turn_ard_time,end=" ")
        print(" Wait Time ", wait_time)
        counter = 0 #reset boolean

  if(i == limit - 1): #If all processes done, go to the first process
      i=0 

  elif(at[i + 1] <= total): 
      i=i+1 
  else: # If arrrival of next process is more than prev, cont with previous
      i=0
