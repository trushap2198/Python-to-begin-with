import numpy as np
import scipy

def hillCipher(plaintext,key):
	cipher = np.matmul(key,plaintext) % 26
	print("cipher",cipher)
	return cipher

def decodeHillCipher(cipher,key):
	denom = int((np.linalg.det(key)%26)-26)
	print(denom)
	temp = 0
	for i in range(1,abs(denom+26)):
		temp = (denom*i)%26
		if (temp == 1):
			temp = i
			break
	print(temp)
	key = np.matrix(key)
	print(key)
	key = key.getH()
	print(key)
	key = np.array(key)
	print(key)
	newKey = key*temp % 26
	print(newKey)
	plaintext = np.matmul(newKey,cipher)%26
	return plaintext
	
	
	
inp = input("Enter the plain text: ")
key = np.array([[17,17,5],[21,18,21],[2,2,19]])

plaintext = []
for i in inp:
	plaintext.append(abs(ord(i)-97))
print("palin",plaintext)
	
iterations  = int(len(plaintext)/3)
answer = []
temp = []

for i in range(0,iterations):
	temp  = hillCipher(plaintext,key)
	i += 3
	#answer.append(temp)
	for j in temp:
		answer.append(j)

print("The encrypted text is: ",end='')

for i in answer:
	print(chr(i+97),end='')
	
print()
print("The decrypted text is: ",end='')
deciphered = decodeHillCipher(answer, key)	
#print(deciphered)
for i in deciphered:
	print(chr(i+97),end='')
