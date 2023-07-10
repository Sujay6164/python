L = ["machine learning\n", "deep learning\n", "augumented reality\n", "virtual reality\n"]
file1 = open('myfile.txt', 'w')
file1.writelines((L))
file1.close()
file1 = open('myfile.txt', 'r')
count = 0
while True:
	count += 1
	line = file1.readline()
	if not line:
		break
	print("Line{}: {}".format(count, line.strip()))
file1.close()
