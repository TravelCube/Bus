import sqlite3

conn = sqlite3.connect('shapes.sqlite')
c = conn.cursor()
c.execute('select * from shapes')
l = c.fetchall()
#c.execute('create table test (s_lat float, s_lot float, e_lat float, e_lon float, ids string)')
print 'start'
r = {}
for i in range(0,len(l)-1):
	start = l[i]
	end = l[i+1]
	if start[3] == end[3]-1:
		line = (start[1],start[2],end[1],end[2])
		if line not in r:
			r[line] = []
		r[line].append(start[0])
	else:
		print 'next' + str(len(r))

for a in r:
	sql = 'insert into test values ({0},{1},{2},{3},"{4}")'.format(a[0],a[1],a[2],a[3],';'.join(r[a]))
	print sql
	c.execute(sql)

conn.commit()
c.close()
