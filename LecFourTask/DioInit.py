list = []

port = input(" plz ente the port (a,b,c,d)")

if port == 'A' or port == 'B' or port == 'C' or port == 'D':

    file = open("/home/hossam/Desktop/EmLx_task/LecFourTask/file.text",'w')
    i = 0
    while i <= 7:
        mode = (input(f"Please Enter Bit {i} mode: "))
        if mode== '0':
            list.append('0')
            i+=1
        elif mode == '1':
            list.append('1')    
            i+=1
        else:
            print("Wrong mode")
            
    list = list[::-1]
    file.write(f'void Init_PORT{port}_DIR(void)\n{{\nDDR{port} =0b{"".join(list)}; \n}}')
else:
    print('wrong port')