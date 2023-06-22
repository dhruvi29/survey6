import subprocess
import time
from dotenv import load_dotenv
from datetime import datetime
import os
import sys
from os import environ
import utils
import config 




capture_path = config.CAPTURE_PATH
backup_path = config.BACKUP_PATH
log_path = config.LOG_PATH

logfilename = "survey6_backup"+ datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
logger = utils.getLogger(logfilename)

rsynclogfilepath = "{}/{}.log".format(log_path,"survey6_rsync"+ datetime.now().strftime("%m-%d-%Y-%H-%M-%S"))

if not os.path.exists(capture_path):
    logger.error("Capture path doesnot exist")
    sys.exit(0)

if not os.path.exists(backup_path):  
    try: 
        os.makedirs(backup_path)
    except OSError as e:
        logging.error(e)
        sys.exit(0)


if __name__ == '__main__':

    f = open(rsynclogfilepath, "w")
    while True:
        # Transfer files to the server using RSync
        cmd = "rsync -partial -z -e 'ssh -p 22' {} {}".format(capture_path,backup_path)
        try: 
	        return_code = subprocess.call(cmd,shell=True,stdout=f)
	        if return_code == 0:
	            logger.info("Rsync Command executed successfully.")
	        else:
	            logger.error("Rsync Command failed with return code {}".format(return_code))
        except Exception as e:
            logger.error(e)

	    # Wait for some time before transferring files again
        time.sleep(60)
        
