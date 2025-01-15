'''
Soecifically for python beginners
Author: Arta Khosravi
Last edit: Jan. 2025
'''
list = [3,4,'arta',5] #LIST
dict = {'arta':19.5, 'khosravi':20} #DICTIONARY
print(list,list[0])
print(dict,dict['arta'])
print(type(list),type(dict)) ##<class 'list'> <class 'dict'>
second_list = ['khosravi',120,34,5]
list.extend(second_list) #adds to lists together
print(list) # 5 was included twice
#-------------------------#
print(list.pop()) #removes list elements
empty_list = []
empty_list.append(list) #drops something to a list
print(list,'vs.',empty_list)