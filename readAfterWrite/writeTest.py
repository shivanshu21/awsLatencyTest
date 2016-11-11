import os
import sys
import time
import dssSanityLib
from boto.s3.key import Key
from datetime import datetime

###################### MAIN ########################

def main(argv):

    ## PARAM OVERRIDES
    dssSanityLib.GLOBAL_DEBUG = 1

    ret = dssSanityLib.fetchArgs(argv)
    if(ret == -1):
        sys.exit(2)

    userObj = dssSanityLib.getConnection(0)
    b = userObj.get_bucket('readafterwrite001kurma')
    k = Key(b)
    for i in range(1, 11):
        k.key = 'testobj' + str(i)
        k.set_contents_from_filename('syslog.2.gz')
        print ("Wrote testobj" + str(i) + " at: "+ str(datetime.now()))
        time.sleep(10)

    print ("Deleting all objects...")
    for k in b.list():
        k.delete()

    return

if __name__ == "__main__":
    main(sys.argv[1:])
