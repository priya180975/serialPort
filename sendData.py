import serial,keyboard,time

ser=serial.Serial(port='COM8',baudrate=9600,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)
print(ser)
#port name
#baudrate -rate at which information is transferred
#bytesize 8bits
#timeout to come out of readloop
#stopbits the number of bits used to indicate the end of a byte

print(ser.isOpen())
print(ser.portstr)


while True:
    print("Sending Message...")
    ser.write("13\r\n".encode("Ascii"))
    time.sleep(1)

    if keyboard.is_pressed("q"):
        print("User needs to quit the application")
        break

ser.close()
print(ser.isOpen())