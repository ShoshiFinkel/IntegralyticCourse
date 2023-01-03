import sys
import datetime
def welcome():
    name = sys.argv[1]
    now = datetime.datetime.now()
    print('Welcome to class', name,'.')
    print('The time now is:', now,'.')

welcome()
