#!/usr/bin/env python
 
'''
single_command.py - execute a single command over ESL
'''
from optparse import OptionParser
import sys
 
import ESL
 
 
def main(argv):
    parser = OptionParser()
    parser.add_option('-a', '--auth', dest='auth', default='ClueCon',
                      help='ESL password')
    parser.add_option('-s', '--server', dest='server', default='127.0.0.1',
                      help='FreeSWITCH server IP address')
    parser.add_option('-p', '--port', dest='port', default='8021',
                      help='FreeSWITCH server event socket port')
    parser.add_option('-c', '--command', dest='command', default='status',
                      help='command to run, surround multi-word commands in ""s')
 
    (options, args) = parser.parse_args()
 
    con = ESL.ESLconnection(options.server, options.port, options.auth)
 
    if not con.connected():
        print 'Not Connected'
        sys.exit(2)
 
    # Run command
    e = con.api(options.command)
    if e:
        print e.getBody()
 
if __name__ == '__main__':
    main(sys.argv[1:])
