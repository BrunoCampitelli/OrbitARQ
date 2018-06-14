# TODO:

# make single uart command
# add read/write functionality
#     for writing to memory, first modify the memory instantiated then re-write 
#     it to the file
# make settings for text file and serial port at the beginning clear
# make infinite loop so you dont have to run just once every time

import serial

st = serial.Serial('COM3',115200, timeout=None,parity=serial.PARITY_NONE, rtscts=0)
print("preparing to read file")
open("rom.txt", 'r').close()
rom=open("rom.txt","r")
memory=list(rom.read())
rom.close()
print("file read")

##########################################################################TEST##########################################################################
##########################################################################TEST##########################################################################
##########################################################################TEST##########################################################################
# address=0
# size=256
#
# print("Requested address:"+str(address))
# print("Requested size:"+str(size))
# #setup pkt to be sent
# pkt=memory[address]
# for n in range(1,size-1):
#     pkt=pkt+memory[address+n]
#
# print(pkt)
#
# address=1853
# size=144
#
# print("Requested address:"+str(address))
# print("Requested size:"+str(size))
# #setup pkt to be sent
# pkt=memory[address]
# for n in range(1,size-1):
#     pkt=pkt+memory[address+n]
#
# print(pkt)
#
# address=9756
# size=13
#
#
# print("Requested address:"+str(address))
# print("Requested size:"+str(size))
# #setup pkt to be sent
# pkt=memory[address]
# for n in range(1,size):
#     pkt=pkt+memory[address+n]
#
# print(pkt)
#
# while 1:
#     pass
##########################################################################TEST##########################################################################
##########################################################################TEST##########################################################################
##########################################################################TEST##########################################################################

while 1:
    cmd='\n'
    cmd=st.readline()#wait for command

    if (cmd[0]=='r'):
        address=cmd[1]
        address=address.decode("utf-8")
        # address=address.strip('\n')
        # address=address.strip(u'\x00')
        address=int(address)
        size=cmd[2]
        size=size.decode("utf-8")
        # size=size.strip('\n')
        # size=size.strip(u'\x00')
        size=int(size)

        #setup pkt to be sent    
        pkt=memory[address]
        for n in range(1,size):
            pkt=pkt+memory[address+n]
        
        #send pkt
        st.write(pkt)

        print(st.read(size+2))#check what stm received


    elif(cmd[0]=='w'):
        address=cmd[1] #get address to be written to
        address=address.decode("utf-8")
        address=int(address)
        
        for n in range(2,len(cmd)-2):
            memory[address+n-2]=cmd[n]#modify instantiated memory
        
        open("mem.txt", 'w').close()#update physical memory
        txtmem=open("mem.txt","w")
        txtmem.write(memory)
        txtmem.close()
        
    else:
        print("invalid command\n")

