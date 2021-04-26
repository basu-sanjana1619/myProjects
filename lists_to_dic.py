#convert list to dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic = {}
for k,v in zip(keys,values):
 dic[k] = v
print(dic)
