def make_all_palindromes2():
	a = []
	for i in range(1,10):
		a.append(str(i) + str(i))
	return(a)

def make_all_palindromes3():
	b = []
	for i in range(10):
		for j in range(10):
			b.append(str(i) + str(j) + str(i))
	return(b)

def check_if_palindrome(s):
	l = len(s)
	for i in range(int(l/2)):
		if(not(s[i]==s[l-i-1])):
			return False
	return True


def main():
	a = make_all_palindromes2()
	b = make_all_palindromes3()
	for num3 in b:
		for num2 in a:
			if (check_if_palindrome(str(int(num3)+int(num2))) and (int(num3)+int(num2)) > 1000):
				print(str(int(num2)+int(num3)) + " = " + str(num3) + " + " + str(num2))


main()