import MySQLdb

class Con:

    global conn

    def __init__(self):
        self.conn = MySQLdb.connect(host="127.0.0.1", db='itspe', user='user', passwd='password')
        self.cur = self.conn.cursor()
        self.conn.autocommit(True)

    def close(self):
        self.cur.close()
        self.conn.close()

'''
con = Con()
curr = con.cur
query = "select DISTINCT `SystemCodeNumber` from utmc_detector_dynamic"
curr.execute(query)
result = curr.fetchall()

for ele in result:
    print(ele[0])

con.close()
'''