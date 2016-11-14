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
    b = userObj.get_bucket('readafterwrite000kurma')
    i = 1
    j = 0
    while (i < 11 and j < 10):
        j = j + 1
        k = Key(b)
        keystring = 'testobj' + str(i)
        k.key = keystring
        try:
            k.get_contents_to_filename(keystring)
            print ("Read " + keystring + " at: "+ str(datetime.now()))
            i = i + 1
        except:
            print("====          Read failed at: " + str(datetime.now()))
            i = i

    return

if __name__ == "__main__":
    main(sys.argv[1:])
