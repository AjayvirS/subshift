# subshift

usage: <program name> [-n new_location] [-r newName] \<source srt\> \<shift by\>


\<source srt\>: the source srt

\<shift by s seconds\>: shift by s seconds, can be a floating point value and/or a negative value

-n: create new srt file in a new location, option arg = new location, if this option is not given, the srt is saved in the same
directory as the old srt file. Furthermore, if the following -r argument isn't given, then the initial srt file is truncated instead

-r: rename to be created srt file, option arg = new name, if this option is not given, the name of source srt is used
