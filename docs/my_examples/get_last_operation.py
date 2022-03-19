# must open with message
with open('messages.txt','r') as f:
    data = f.readlines()
    operation_message = ''
    #for line in range(0,len(data),-1):
    for line in range(-6,0):
        operation_message+=str(data[line]) 

print(operation_message)

f.close()