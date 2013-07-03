'''this program will take a file containing a string of DNA and find it's reverse complement.
It is important to remember to not just find the complements according to how base pairs are formed,
but to also reverse the order as one strand runs bottom up, and the other strand top down.'''

f = open('string.txt', 'r')
s = f.read() #our DNA string.
f.close()
sc = "" #null initialization of DNA strings complement.

for i in s:
	if i == 'A':
		sc += 'T'
	elif i == 'T':
		sc += 'A'
	elif i == 'C':
		sc += 'G'
	elif i == 'G':
		sc += 'C'

f = open('strComp.txt', 'w')
sc = sc[::-1]
f.write(sc)
f.close()
print (sc)
	