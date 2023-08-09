'''
write a python program to count the number 4 in a given list
Name : Hossam Adel Mostafa

'''

Items_Number = int(input("plz entre the number of array\n"))
My_Array = []
for i in range (Items_Number) :
    index = int(input("entre the indix of  array\n"))
    My_Array.append(index)
Num = int(input("plz entre the num to search\n"))
counter = My_Array.count(Num)
print(f"number occuers {counter} ")



