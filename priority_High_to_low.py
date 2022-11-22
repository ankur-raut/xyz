n=4
abt=[5,4,2,1]
at=[0,1,2,4]
p=[10,20,30,40]
bt = [[5,0,10,0], [4,1,20,1], [2,2,30,2], [1,4,40,3]]

sumbt = 0 
i = 0
ll = []
for i in range(0, sum(abt)): 
	l = [j for j in bt  if j[1] <= i] #Appending all processes which are less than cureent second. ready queue
	l.sort(key=lambda x: x[2], reverse=True) #Sort on basis of priority. high to low
	print(l)
	bt[bt.index(l[0])][0] -= 1 #Reducing the Burst Time of that process by 1
	for k in bt:
		if k[0] == 0: #If a process has been completed remove it.
			bt.pop(bt.index(k))
			ll.append([k, i + 1]) #Whichever process is donw, that is being saved here. i+1 is completion
print(ll)
ct = [0] * (n)
tat = [0] * (n)
wt = [0] * (n)
for i in ll:
	ct[i[0][3]] = i[1] 


for i in range(len(ct)):
	tat[i] = ct[i] - at[i]
	wt[i] = tat[i] - abt[i]

print('P\tBT\tAT\tCT\tTAT\tWT')
for i in range(len(ct)):
	print("{}\t{}\t{}\t{}\t{}\t{}\n".format(p[i],abt[i], at[i], ct[i], tat[i], wt[i]))