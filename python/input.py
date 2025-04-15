# f=open("demo.txt", "r")
# data=f.read(5)
# print(data)
# print(type(data))
# f.close()

#line by line read
# f=open("demo.txt", "r")
# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)
# f.close()

# f=open("demo.txt", "w")
# f.write("my name is pratibha vishwakarma and currently i am pursuing mca from knct group of college of bhopal")
# f.close() 

# f=open("demo.txt", "r+")
# f.write("pratibha")
# f.read() 
# f.close()
#a+ mode is used to read and write both
#r+ mode is used to read and write both but it will not create a file if file is not present and overwrite the file and starting from the begining
#w+ mode is used to read and write both but it will create a file if file is not present

#with syntax
# with open("demo.txt", "r") as f:
#     data= f.read()
#     print(data)
count=0
with open("demo.txt", "r") as f:
    data= f.read()
    print(data)
    
    nums=data.split(",")
    for val in nums:
       if(int(val)%2==0):
           count+=1
print(count)
    
   
    # num=""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #         print(int(num))
    #         num=""
    #     else:
    #         num += data[i]    
    