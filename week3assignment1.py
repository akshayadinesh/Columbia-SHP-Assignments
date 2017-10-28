import time

def progress_bar(seconds):
	print("ran")
	seconds_per_X = int(seconds)
	seconds_per_X /= 10
	print(seconds_per_X)
	for i in range(10):
		time.sleep(seconds_per_X)
		print("X")
secondsInput = input("How many seconds? ")
progress_bar(secondsInput)
