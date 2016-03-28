import uuid

def genaratorActiveCode(number=200):
	result = []
	while True is True:
		uuid_id=uuid.uuid1()
		tem=str(uuid_id).replace('-','')
		tmmm=str(tem[4:])
		if not tmmm in result:
			result.append(tmmm)
		if len(result) is number:
			break
	print result
	
if __name__=='__main__':
	genaratorActiveCode(10)
	print"Finished."