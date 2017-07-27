def main():
	a='this is a sentence'
	print(myfunctn(a))

def myfunctn(string):
	return string[0:5]+' this is a test'

if __name__=='__main__':
	main()
