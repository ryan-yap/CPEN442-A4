import hashlib
import time

start_time = time.time()
hashPwd = "im1ED8C03CBAF3D7753C0D8D9C2A904D1682696154"
noSalt = hashPwd[2:].lower()
# f = open('myfile.txt','w')
i = 0
ifFound = False
while (i<10000 and not ifFound):
	stringNum = ""
	if(i<=9):
		stringNum = "000" + str(i)
	elif(i>9 and i<=99):
		stringNum = "00" + str(i)
	elif(i>99 and i<=999):
		stringNum = "0" + str(i)
	else:
		stringNum = str(i)
	stringNum = "im" + stringNum
	hashValue = str(hashlib.sha1(stringNum).hexdigest())
	# f.write(hashValue + '\n')
	if(hashValue == noSalt):
		ifFound = True
		endtimestamp = int(time.time())
		print("The password is " + stringNum)
		print("--- %s seconds ---" % (time.time() - start_time))
		break
	i=i+1

if(not ifFound):
	print("No Hash Found!")
# f.close()