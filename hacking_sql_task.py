import MySQLdb
import lib.mysql_lib as mysql_lib
def main():
    db = MySQLdb.connect(host="HOSTNAME", # your host, usually localhost
                         user="USERNAME", # your username
                          passwd="passwd", # your password
                          db="db name") # name of the data base
    cur = db.cursor()
    cur.execute("SELECT user_id FROM users")
    rows = cur.fetchall()

    for row in rows:
        userid = row[0]
        a = score_puppet(userid,cur)
        print a
        b = score_blockedsites(userid,cur)
        print b
        c = score_munki(userid,cur)
        print c
        d = score_lastpass(userid,cur)
        print d
        e = score_2facdash(userid,cur)
        print e
        total = totalscore(userid,a,b,c,d,e)
        print total
    #user_id = mysql_lib.user_id_from_username("mschnugg")
    # Use all the SQL you like
def score_puppet(userid,cur):
    score_p = 0
    cur.execute("SELECT * FROM puppet WHERE user_id = %d" % userid)
    rows = cur.fetchall()
    if not cur.rowcount:
        print "No results found"
        return 0
    else:
        for row in rows:
            print row
            print row[1]
            print row[2]
            print row[3]
            score_tmp = int(row[1]) + int(row[2]) + int(row[3])
            print score_tmp
            if score_tmp == 3:
                score_p = 300
            elif score_tmp == 2:
                score_p = 200
            elif score_tmp == 1:
                score_p = 100
            else:
                score_p = 0

        return score_p
def score_blockedsites(userid,cur):
    score_o = 0
    cur.execute("SELECT * FROM org2blockedsites WHERE user_id = %d" % userid)
    rows = cur.fetchall()
    if not cur.rowcount:
        print "No results found"
        return 0
    else:
        for items in rows:
            print items
            print int(items[1])
            if int(items[1])==0:
                score_o = 100
            elif int(items[1]) > 6:
                score_o = 0
            elif int(items[1])>=1 and int(items[1])<=5:
                score_o = 50
        return score_o

def score_munki(userid,cur):
    score_m = 0
    cur.execute("SELECT * FROM munki WHERE user_id = %d" % userid)
    rows = cur.fetchall()
    if not cur.rowcount:
        print "No results found"
        return 0
    else:
        for m in rows:
            print m
            print m[4]
            score_m = 100
            """if int(m[4]) == '\x00':
                score_m = 100
            else:
                score_m = 0"""
        return score_m

def score_lastpass(userid,cur):
    score_l = 0
    cur.execute("SELECT * FROM lastpass WHERE user_id = %d" % userid)
    rows = cur.fetchall()
    print rows
    if not cur.rowcount:
        print "No results found"
        return 0
    else:
        for n in rows:
            #print n
            score_l = int(n[1]) + int(n[2]) + int(n[3])
        return score_l

def score_2facdash(userid,cur):
    score_f = 0
    cur.execute("SELECT * FROM 2FacDash2 WHERE user_id = %d" % userid)
    rows = cur.fetchall()
    print rows
    if not cur.rowcount:
        print "No results found"
        return 0
    else:
        for t in rows:
            print t[1]
            if t[1] > 0:
                score_f = 100
            else:
                score_f = 0
        return score_f

def totalscore(userid,a,b,c,d,e):
    total_score = a + b + c + d + e
    print "the total score of user"+str(userid), total_score
    return total_score

if __name__ == "__main__":
    main()