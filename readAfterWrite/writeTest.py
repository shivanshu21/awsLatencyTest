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
    bucket_name = 'readafterwrite003kurmaeu'

    ret = dssSanityLib.fetchArgs(argv)
    if(ret == -1):
        sys.exit(2)

    #userObj = dssSanityLib.getConnection(0)
    userObj = boto.s3.connect_to_region(
                      'eu-west-1',
                      aws_access_key_id=dssSanityLib.user_profiles[0]['access'],
                      aws_secret_access_key=dssSanityLib.user_profiles[0]['secret'],
                      calling_format=boto.s3.connection.OrdinaryCallingFormat())

    bucket = userObj.get_bucket(bucket_name)
    k = Key(bucket)
    for i in range(1, 21):
        k.key = 'testobj' + str(i)
        k.set_contents_from_filename('data')
        print ("Wrote testobj" + str(i) + " at: "+ str(datetime.now()))
        time.sleep(10)

    print ("Deleting all objects...")
    for k in b.list():
        k.delete()

    return

if __name__ == "__main__":
    main(sys.argv[1:])
