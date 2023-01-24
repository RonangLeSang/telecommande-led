# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:23:38 2021

@author: ronan
"""
import paramiko
import time
from tkinter import *
from tkinter import ttk

val1 = 0
val2 = 0
val3 = 0

def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

def lance():
    stdin,stdout,stderr=ssh_client.exec_command("/usr/bin/hyperiond")
    time.sleep(3)
    
def quitte():
    stdin,stdout,stderr=ssh_client.exec_command("killall hyperiond")
    time.sleep(3)

def voir():
    cnv=Canvas(root, width=600, height=400, bg=(rgbtohex(val1,val2,val3))).grid(column=0, row=4)
    
def value1(val):
    global val1
    val1 = int(float(val))
    voir()
   
def value2(val):
    global val2
    val2 = int(float(val))
    voir()
   
def value3(val):
    global val3
    val3 = int(float(val))
    voir()
    
def envoi():
    quitte()
    chaine = "echo " + str(val1) + "l>/home/pi/coucou.txt"
    stdin,stdout,stderr=ssh_client.exec_command(chaine)
    chaine = "echo " + str(val2) + "l>>/home/pi/coucou.txt"
    stdin,stdout,stderr=ssh_client.exec_command(chaine)
    chaine = "echo " + str(val3) + "l>>/home/pi/coucou.txt"
    stdin,stdout,stderr=ssh_client.exec_command(chaine)
    time.sleep(0.5)
    stdin,stdout,stderr=ssh_client.exec_command("python3 /home/pi/hue.py")
   

ip_address = "192.168.1.54"
username = "pi"
password = "terrasnet"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)
print("Successfully connected to", ip_address)

remote_connection = ssh_client.invoke_shell()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Contrôle LED").grid(column=0, row=0)
ttk.Button(frm, text="lance", command=lance).grid(column=1, row=0)
ttk.Button(frm, text="quitte", command=quitte).grid(column=0, row=0)
ttk.Button(frm, text="envoi", command=envoi).grid(column=2, row=0)


ttk.Label(frm, text="rouge").grid(column=0, row=1)
w1 = ttk.Scale(root, from_=0, to=255,command=value1).grid(column=0, row=1)
ttk.Label(frm, text="bleu").grid(column=0, row=2)
w2 = ttk.Scale(root, from_=0, to=255,command=value2).grid(column=0, row=2)
ttk.Label(frm, text="vert").grid(column=0, row=3)
w3 = ttk.Scale(root, from_=0, to=255,command=value3).grid(column=0, row=3)

root.mainloop()



ssh_client.close