num = input('Input:')
num = int(num)
# num_list=[]
count=0
for i in range(1,num+1):
    if(i%3!=0 and i%5!=0):
#         num_list.append(i)
        count=count+1
    if(i%3==0 and i%5==0):
#         num_list.append(i)
        count=count+1
        
print(count)