def getHeader(filename):
	headers = []
	headerNeed = ['Cookie','User-Agent']
	with open(filename,'r') as fp:
		for line in fp.readlines():
			name,value = line.split(':',1)
			if name in headerNeed:
				headers.append((name.strip(),value.strip()))
	return headers

if __name__ =='__main__':
	headers  = getHeader('headerRaw.txt')
	print(headers)

