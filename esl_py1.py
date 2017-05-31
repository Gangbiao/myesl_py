#!/usr/bin/env python
 
'''
events.py - subscribe to all events and print them to stdout
'''
import ESL
 
con = ESL.ESLconnection('localhost', '8021', 'ClueCon')
 
if con.connected:
    con.events('plain', 'all')
    while 1:
        e = con.recvEvent()
        if e:
            print e.serialize()