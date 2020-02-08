
import sys
import os
import getopt
from datetime import datetime, timedelta

#usage: <program name> [-n:] [-r:] <source srt> <shift by s seconds>
# -n: create new srt file in a new location, option arg = n, if this option is not given, the srt is saved in the same
# directory as the old srt file. Furthermore, if the following -r argument isn't given, then the initial srt file is truncated instead
# -r: rename to be created srt file, option arg = new name, if this option is not given, the name of source srt is used


argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv, 'n:r:h', ['new_location=', 'rename=', 'help'])
except getopt.GetoptError:
        sys.exit('Usage: %s [-n location] [-r filename]' % sys.argv[0])

#check if both arguments are given
if len(args) < 2:
    sys.exit('Usage: %s [-n location] [-r filename] <source srt> <shift_by>' % sys.argv[0])

#extract directory name for storing the new srt
path = os.path.dirname(args[0])

#name of srt file is same as old one, unless specified otherwise
newName = os.path.basename(args[0])

#time to shift, can be positive/negative/floating-point value
shiftBy = float(args[1])

#the older srt file
oldFile = args[0]

for opt, arg in opts:
    if opt in ('-h', '--help'):
        sys.exit('Usage: %s [-n location] [-r filename]' % sys.argv[0])
    elif opt in ('-n', '--new_location'):
        path = arg
    elif opt in ('-r', '--rename'):
        newName = arg
    else:
        sys.exit('Usage: %s [-n location] [-r filename]' % sys.argv[0])

#if the directory and the path do not exist, make a new one to store new file there
if not os.path.exists(path):
        os.makedirs(path)

#handle special case, if specified directory ends with '/'
if path[-1] == '/':
    path = path[:-1]

newFile = open(path+'/'+newName+'.srt', 'w')

#the actual shifting occurs here, the values are read from the older srt file, modified and stored in the newer specified file
#(or the same file is truncated if no -r and -n arguments are given)
with open(oldFile, 'r') as my_file:
    for line in my_file:
        if '-->' in line:
            try:
                db_begin = datetime.strptime(line[:11], '%H:%M:%S,%f')
                newTime_begin = db_begin + timedelta(0,shiftBy)
                db_end = datetime.strptime(line[18:28], '%H:%M:%S,%f')
                newTime_end = db_end + timedelta(0,shiftBy)

                str1 = newTime_begin.strftime('%H:%M:%S,%f')
                str2 = newTime_end.strftime('%H:%M:%S,%f')
                newFile.write(str1[:11] + ' ' + '-->' + ' ' + str2[:11])
                newFile.write(os.linesep)
            except ValueError:
                print('Subtitle not shifted, invalid time format: %s' % line)
                continue
        else:
            newFile.write(line.rstrip())
            newFile.write(os.linesep)