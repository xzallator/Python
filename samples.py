import hashlib
import sqlite3

conn = sqlite3.connect("userdata04.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata04(
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    PASSWORD VARCHAR(255) NOT NULL
)
""")

username1,password1 = "EXELINT",hashlib.sha256("EXELINTpassword".encode()).hexdigest()
username2,password2 = "DANGJIER",hashlib.sha256("DANJ99".encode()).hexdigest()
username3,password3 = "PANDHU88",hashlib.sha256("PANDHU89".encode()).hexdigest()
username4,password4 = "BRODIAZ",hashlib.sha256("BRODIAZpassword".encode()).hexdigest()
username5,password5 = "CONQUEROR",hashlib.sha256("CONQUERORpassword".encode()).hexdigest()

cur.execute("INSERT INTO userdata04(username,password)VALUES(?,?)",(username1,password1))
cur.execute("INSERT INTO userdata04(username,password)VALUES(?,?)",(username2,password2))
cur.execute("INSERT INTO userdata04(username,password)VALUES(?,?)",(username3,password3))
cur.execute("INSERT INTO userdata04(username,password)VALUES(?,?)",(username4,password4))
cur.execute("INSERT INTO userdata04(username,password)VALUES(?,?)",(username5,password5))

conn.commit()
