## circle is now a module
import circle as c

def main():
	radiusA = 3
	print('{:.2f}'.format(c.circumference(radiusA)))
	print(variableLengthPosPar(3,4,"hello", True, 3))
	print(variableLengthKeywordPar(3,5,bob=1,sally=2))
	#print(reverse("python"))
	tuple1 = (1,3,8, 'hey')
	print(tuple1)
	s1={5,4,4,10}
	s2={5,4,1}
	print(s1.union(s2))

def pi():
	pi = c.math.pi
	print(pi)

def keywordPar(a, b=5):
	print(a)
	print(b)

def variableLengthPosPar(a, b, *c):
	print(a)
	print(b)
	print(c)

def variableLengthKeywordPar(a,b,**d):
	for item in d:
		print(item)

def reverse(s):
	if len(s)==1:
		return s
	else:
		new_string = s[len(s)-1] + reverse(s[0:len(s)-1])

main()






