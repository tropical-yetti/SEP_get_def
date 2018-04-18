# SEP_get_def
SEP_get_def is a python script to download new AV definitions from Symantec site.

Please, change the 'path' var for one you prefer. It needed to be a empty dir as in the end the SEP_get_def will clean the dir leaving only the x32 and x64 files for the newest definitions installers.

ATTENTION! If you refer to a non empty folder SEP_get_def will delete all the files in the path folder.

There is a 'double check' to be sure that the working dir is equal to path but it's supposed that you are sure that path refers to an empty folder.

You can save SEP_get_def.py in the path folder too. SEP_get_def.py will create a log file also in it.
