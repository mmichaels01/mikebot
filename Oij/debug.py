import sys
print sys.path

import ptvsd
ptvsd.enable_attach(secret = None, address=('0.0.0.0', 23))
print "Wting for attach"
ptvsd.wait_for_attach()


try:
    print 'test'
    five = raw_input()
except KeyboardInterrupt:
    print 'done'