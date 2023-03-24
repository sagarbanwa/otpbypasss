''' This script will grnrate 4 and 6 digit of OTP brutr force pins based on config above 
it could be 

{"otp":["0001
         0002
         0003
         0004
         005"
    ]
}

'''

#python script.py 
#output will be saved in text file 6_digitOTP.txt open with any notepad draga and drop 

numbers = []
#for i in range(10000): #if u need to do the same for 0000-9999
for i in range(1000000): #if u need to do the it for 000000-99999
    number = str(i).zfill(6)
    numbers.append(number)

with open("6_digitOTP.txt", "w") as f:
    for number in numbers:
        f.write(number + "\n")
