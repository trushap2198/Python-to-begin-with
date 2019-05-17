import string
fh=open("goat.txt")
count=dict()
char=[]
for line in fh:
	line=line.translate(string.punctuation)
	line=line.lower()
	words=line.split()
	num=0;
	for w in words:
		char.append(tuple(w))
	for word in char:
		for letters in word:
			num+=1;
		count[word]=num;
		num=0;
	
			
print(count);
