daily_task=["Exercise-","breakfast","1st coding","lunch break","2nd coding","snacks break","english and recreation activity","dinner break","Extra study"]
completed_task=["Exercise","breakfast","1st coding","lunch break"]
a=len(daily_task)
b=len(completed_task)
i=0
c=0
d=[]
while i<a: 
    if daily_task[i] not in completed_task:
        d.append(daily_task[i])
        c=c+1
    i=i+1
print("number of lefted task:",c)
print("lefted task is:",d)