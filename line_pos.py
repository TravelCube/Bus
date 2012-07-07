import sqlite3

conn = sqlite3.connect('./DB/tranz.sqlite')
conn.text_factory = str
c = conn.cursor()

def Query(sql):
	print sql
	c.execute(sql)
	l = c.fetchall()
	print len(l)
	return l

def GetFirst(l):
	return [r[0] for r in l]

def getRoutesIds(bus_line):
	sql = 'select id from routes where bus_num = {0}'.format(bus_line)
	c.execute(sql)
	l = c.fetchall()
	print [r[0] for r in l]
	return [r[0] for r in l]

def getTripsIdsfromRoutes(routes_ids):
	sql = 'select service_id from trips where route_id in {0}'.format(tuple(routes_ids))
	l = GetFirst(Query(sql))
	print l
	return l

def getServiceIdsFromTripsIds(trips_ids):
	sql = 'select service_id from trips where id in {0}'.format(tuple(trips_ids))
	l = GetFirst(Query(sql))
	print l
	return l

def getServiceIdsinDay(fullService_ids, day):
	sql = 'select service_id from calendar where {0} = 1 and service_id in {1}'.format(day,tuple(fullService_ids))
	print sql
	c.execute(sql)
	l = c.fetchall()
	print [r[0] for r in l]
	return [r[0] for r in l]

def getShapesIdsfromServiceIds(service_ids):
	sql = 'select distinct shape_id from trips where service_id in {0}'.format(tuple(service_ids))
	l = GetFirst(Query(sql))
	print l
	return l

pl = getRoutesIds(921)
pl = getTripsIdsfromRoutes(pl)
pl = getServiceIdsinDay(pl, 'sunday')
pl = getShapesIdsfromServiceIds(pl)

c.close()
conn.close()
