#function is a block of statement that perform a specific task.
# zip () function is used to combine two list.
# map() function is used to apply a function to all the items in an input_list.
# name=['john','Alice','Bob','pratibha']
# score=[90,80,70,60,90]

# res=zip(name,score)
# print(list(res))



# a=[1,2,3,4]
# b=['a','b','c']

# res=zip()

# print(list(res))
# res=zip(a)
# print(list(res))

# res=zip(a,b)
# print(list(res))





# a=[('Apple',10), ('Banana', 20), ('orange',30)]

# fruits,quantities=zip(*a)

# print(f"fruits={fruits}")
# print(f"quantities={quantities}")



# d={'name': 'john', 'age':25,'grade':'A'}

# keys=d.keys()
# values=d.values()

# res=zip(keys,values)
# print(list(res))

#pickling and unpickling in python is used to serialize and deserialize a python object structure.
# import pickle
# person={
#     "name":"pratibha",
#     "age":24,
#     "gender":"male"
# }

# with open("person.pickle","wb") as file:
#     pickle.dump(person, file)
# print("pickling completed")    



# import pickle
# with open('data.pkl','rb' )as f:
#     data=pickle.load(f)
    
# print(data)    
