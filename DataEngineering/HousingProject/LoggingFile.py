import os
import sys

CURR_DIR = os.path.dirname(__file__)
sys.path.append(CURR_DIR)
LOG_FOLDER =  CURR_DIR + '/logs'
LOG_FILE = 'housing_logs.txt'