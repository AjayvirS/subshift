# subshift

usage: <program name> [-n:] [-r:] \<source srt\> \<shift by s seconds\>
  
-n: create new srt file in a new location, option arg = n, if this option is not given, the srt is saved in the same
directory as the old srt file. Furthermore, if the following -r argument isn't given, then the initial srt file is truncated instead

-r: rename to be created srt file, option arg = new name, if this option is not given, the name of source srt is used
