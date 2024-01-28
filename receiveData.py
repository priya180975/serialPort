import serial,keyboard,time,requests

ser=serial.Serial(port='COM7',baudrate=9600,bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)
url='http://localhost:8000/weightdata'
head = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJQcml5YSIsImV4cCI6MTcwNjQzOTAzMn0.OxXKpZ_XSXkFqFqKRNtyQNiU1kZ5sXFQnB3pZJJUBWA'}

print(ser)
print(ser.isOpen())
print(ser.portstr)

while True:
    print("Receiving Message...")
    receiver=ser.readline()
    serialdata=receiver.decode("Ascii").rstrip()
    if serialdata.isdigit()==False:
        print('Error Weight Value or no weight found')
    else:
        payload={
            "weight":serialdata
        }

        patchrequest=requests.put(url,json=payload,headers=head)
        print("\npatch request",patchrequest)
        print(patchrequest.json())

    time.sleep(1) #delay


    if keyboard.is_pressed("q"):
        print("User needs to quit the application")
        break

ser.close()
print(ser.isOpen())