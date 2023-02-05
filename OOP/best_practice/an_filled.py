import logging
import ctypes.wintypes
import os
import sys

#Find the documents folder on the pc running from
#this code is to find the my documnets path on the computer this is running on
CSIDL_PERSONAL = 5       # My Documents
SHGFP_TYPE_CURRENT = 0   # Get current, not default value
buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
Docs_folder = ''
Docs_folder = buf.value
if Docs_folder == '':
    logging.critical('could not find documents folder and therefore will not find db info not be able to save appending results')
#Find the  AFM folder sitting in the documents folder that contains db connection info and outputs log file
WEDDING_DOCS_FOLDER = Docs_folder + '/wedding_planner'


#hardcoded folder names:
CURR_DIR = os.path.dirname(__file__)
sys.path.append(CURR_DIR)
INFO_FOLDER = CURR_DIR + '/wedding'
LOG_FOLDER =  CURR_DIR + '/logs'
HALLS_INFO_FILE = 'halls.csv'
LOG_FILE = 'wedding_logs.txt'