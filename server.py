import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",9999))

server.listen()

def handle_connection(c):
    c.send("username :".encode())
    username = c.revc(1024).decode()
    c.send("password :".encode())
    password = c.revc(1024).decode()
    password = hashlib.sha256(password).hexdigest()

    conn = sqlite3.connect("userdata04.db")
    cur =  conn.cursor()

    cur.execute("SELECT * FROM userdata04 WHERE username = ? AND password = ?",(username,password))

    if cur.fetchall():
        c.send("Login Successfull!".encode())
    else:
        c.send("Login Failed".encode())

while True:
        client, addr = server.accept()
        threading.Thread(target = handle_connection, args=(client,)).start()