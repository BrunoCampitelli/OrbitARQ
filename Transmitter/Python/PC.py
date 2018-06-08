import serial

st = serial.Serial('COM3',115200, timeout=5,parity=serial.PARITY_NONE, rtscts=0)

#out=1
#st.write(out)
while 1:
    out = st.readline()
    #out=out.decode("utf-8")
    #out=out.strip('\n')
    #out=int(out)
    print(out+1)
    #st.write(out+1)
