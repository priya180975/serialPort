import requests,keyboard,time

# url='https://jsonplaceholder.typicode.com/users/1'
url='http://localhost:8000/weightdata'

payload={
    "weight":100
}

while True:
    # print("\n\nFetch API Data")
    # res = requests.get(url)

    # print("response",res.json())
    # time.sleep(5) #delay

    patchrequest=requests.patch(url,json=payload)
    print("\npath request",patchrequest)
    print(patchrequest.json())


    if keyboard.is_pressed("q"):
        print("User needs to quit the application")
        break

print("end")