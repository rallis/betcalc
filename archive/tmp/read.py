import io,json
from pprint import pprint
x = json.load(open('output.txt'))

s = 1
for item in x['stats']:
	print s, item['timestamp'] #, item['file'], item['lastTimestamp']
	s+=1
