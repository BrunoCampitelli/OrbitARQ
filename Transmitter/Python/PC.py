import serial

st = serial.Serial('COM6',115200, timeout=5,parity=serial.PARITY_NONE, rtscts=0)
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

out=-1
# while 1:
print("waiting for address")

#wait for address
address=-1
while (address<0):
    address=st.readline()

size=st.readline()
    # print("address1:"+address)

address=address.decode("utf-8")
# print("address2:"+address)
address=address.strip('\n')
address=address.strip(u'\x00')
# print("address3:"+address)
address=int(address)
size=st.readline()
size=size.decode("utf-8")
size=size.strip('\n')
size=size.strip(u'\x00')
size=int(size)
    # print("address:"+size)

# address = out
# out = -1
# print("Requested address:"+str(address))

#wait for packet s-ize
# while (out<0):
#     out=st.readline()
#     print("size:"+out)
#     out=out.decode("utf-8")
#     print("size:"+out)
#     out=out.strip('\n')
#     out=out.strip(u'\x00')
#     print("size:"+out)
#     out=int(out)

# size = out
# out = -1
# print("Requested size:"+str(size))

#setup pkt to be sent
pkt=memory[address]
for n in range(1,size):
    pkt=pkt+memory[address+n]

#print(pkt)
#send pkt
st.write(pkt)

# print("checking for output")
print(st.read(size+2))

    # while 1:
    #     pass
