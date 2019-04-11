import os, sys

source_dir = os.path.dirname(os.path.realpath(__file__)) + '/template/'
 
os.system('squarespace-server https://oboe-conch-afl6.squarespace.com/ -d ' + source_dir)