
'''
write a python program to find largst number 
Name : Hossam Adel Mostafa

'''

#first solution

list = [10,50,40,90,100,55]
list.sort()
print("largest element is \n", max(list))


#second solution 

list = [10,50,40,90,100,55]
max = list[0]
for i in range(len(list)) :
    if list[i] > max :
        max = list[i]
print("largest element is \n ", max)

