#!/usr/bin/env python
 
'''
server.py
test
'''
import SocketServer
import ESL
 
class ESLRequestHandler(SocketServer.BaseRequestHandler):
    def setup(self):
        print self.client_address, 'connected!'
 
        fd = self.request.fileno()
        print fd
 
        con = ESL.ESLconnection(fd)
        print 'Connected: ', con.connected()
        if con.connected():
 
            info = con.getInfo()
 
            uuid = info.getHeader("unique-id")
            print uuid
            con.execute("answer", "", uuid)
            con.execute("playback", "/ram/swimp.raw", uuid);
         
# server host is a tuple ('host', port)
server = SocketServer.ThreadingTCPServer(('', 8040), ESLRequestHandler)
server.serve_forever()
