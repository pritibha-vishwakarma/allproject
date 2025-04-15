#print("enter your name ")
#name = input("enterd your name")
#print("welcome miss", name ,"we are very lucky to come with my function you", name)
# int("5")
# val = float(input("enter some value:"))
# print(type(val), val)
                          #sum of two number
# first =int(input("enter first number:"))
# second = int(input("enter second number:"))
# print("sum", first+second)
               #squre side
# side = int(input("enter squuare side:"))
# print("area=" , side*side)


#    wap to input 2 floating numbers and print their average.
#a =float(input("fn"))
#b =float(input("sn"))


#print("avg=", (a+b)/2)
#a =int(input("fn"))
#b =int(input("sn"))
#print(  a>=b)

#concatenation concept in String ...............
#ex "hello"+"world"-----"helloworld"
#str1 = "pratibha "
#str2 = "vishwakarma"
#final_str = (str1+str2)
#print(final_str)
#   length of string 
#len(str)
# str1 = "apna"
# len1 = len(str1)
# print(len1)

# str2 ="college"
# len2 = len(str2)
# print(len2)

# final_str =str1 +"  "+str2
# print(final_str)
# print( len (final_str))
                                     #indexing in pytohn    indexing main value modefi nhi kr skte hai 
# str ="pratibha vishwakarma"
# ch =str[8]
# print(ch)
#     slicing sting ka part krna
# str ="pratibha vishwakarma
# print(str[0:5])
# print(str [0:4])
# print(str[4:len(str)])
# print(str[5:])   length of string tk jata hai
                      #  a= -5  p= -2                                      


# str ="my name is pratibha"
# print(str.find("name"))

# #practice question
# #wap to input user's first  name & print its length 
# name =input("entered users first name ")
# print(" lenght of yourname", len(name))
# str ="hii i am $ symbol e $stablished in 1447:"
# print(str.count("$"))
#print((1,3)*2)



main_dict={}
def insert_item(item):
   if item in main_dict:
       main_dict[item] += 1
   else:
       main_dict[item] = 1
#Driver code
insert_item('Key1')
insert_item('Key2')
insert_item('Key2')
insert_item('Key3')
insert_item('Key1')
print (len(main_dict))


