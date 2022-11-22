# n = int(input('Enter no of processes: '))
# bt = [0] * (n + 1) #list of burst time, arrival time and processID
# at = [0] * (n + 1)# arrival time
# abt = [0] * (n + 1)# burst time
n=4
at=[0,1,2,4]
abt=[5,3,4,1]
bt = [[5, 0, 0], [3, 1, 1], [4, 2, 2], [1, 4, 3]]
# for i in range(n):
# 	abt[i] = int(input('Enter the burst time for process {} : '.format(i + 1)))
# 	at[i] = int(input('Enter the arrival time for process {} : '.format(i + 1))) 
# 	bt[i] = [abt[i], at[i], i]

# print(at) #Printing Arival Time
# print(abt)# burst time
# print(bt) #Printing the list of Burst Time, Arrival Time, ProcessID
# bt.pop(-1) #Removing 0
# print(bt)
sumbt = 0 
i = 0
ll = []
for i in range(0, sum(abt)): 
	l = [j for j in bt  if j[1] <= i] #Appending all processes which are less than cureent second. ready que members
	l.sort(key=lambda x: x[0]) #Sort on basis of Burst Time.
	print(l, l[0][2])
	bt[bt.index(l[0])][0] -= 1 #Reducing the Burst Time of that process by 1
	for k in bt:
		if k[0] == 0: #If a process has been completed remove it.
			bt.pop(bt.index(k))
			ll.append([k, i + 1]) #Whichever process is donw, that is being saved here. i+1 is completion
print(ll)
ct = [0] * (n)
tat = [0] * (n)
wt = [0] * (n)

for i in ll: # completion time map to id
  #ll- [[[0,1, 2], 1]..]
	print(i, i[0], i[1], i[0][2])
	ct[i[0][2]] = i[1] 
	#abt[i[0][3]] = i[0][2]

for i in range(len(ct)):
	tat[i] = ct[i] - at[i]
	wt[i] = tat[i] - abt[i]
# ct.pop(-1)
# wt.pop(-1)
# tat.pop(-1)
# abt.pop(-1)
# at.pop(-1)
print('BT\tAT\tCT\tTAT\tWT')
for i in range(len(ct)):
	print("{}\t{}\t{}\t{}\t{}\n".format(abt[i], at[i], ct[i], tat[i], wt[i]))
print('Average Waiting Time = ', sum(wt)/len(wt))
print('Average Turnaround Time = ', sum(tat)/len(tat))