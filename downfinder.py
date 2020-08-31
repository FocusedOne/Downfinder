import inspect
#dogs = open('/Users/gphillips/cabotping151020.txt')
print 'Which file should I look at?'
file  = raw_input()

dogs = open(file)

if '192.168.171.1' in dogs.readline():
    print 'Reading ping times for Benton'

else: print 'Reading ping times for Cabot'


pings = list(dogs.readlines())

birds = 0

downfrom = 0
downto = 0

downtimes = []

downlist = []

print 'Read %s lines of data' % (len(pings))

#gen = (i for i,x in enumerate(pings) if 'timeout' in x)
#
#for i in gen:
#    downtimes.append(i)
#    birds +=1
#    downlist.append(i)

for l in pings:
    if 'timeout' in l:
        downtimes.append(l)
        birds +=1



#downfrom = downtimes[-1]
#downto = downtimes[1]

if len(downtimes) >= 5:
    downfrom = downtimes[1]
    downto = downtimes[-1]
    print 'Found %s dropped pings from %s to %s' % (birds, downfrom[:19], downto[:19])

else:
    print 'Pipes unclogged, internet good.'

dogs.close()
