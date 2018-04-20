# SEP_get_def
SEP_get_def is a python script to download new AV definitions from Symantec site.

Please, change the 'path' var for one you prefer. It needed to be a empty dir as in the end the SEP_get_def will clean the dir leaving only the x32 and x64 files for the newest definitions installers.

ATTENTION! If you refer to a non empty folder SEP_get_def will delete all the files in the path folder.

There is a 'double check' to be sure that the working dir is equal to path but it's supposed that you are sure that path refers to an empty folder.

You can save SEP_get_def.py in the path folder too. SEP_get_def.py will create a log file also in it.

It's very useful tu set a crontab entry for this script.

To edit crontab table:
$ crontab -e

Add a line like these to crontab:
"# m h  dom mon dow   command"

"# Will run the script three times a day every day"

"0 8,12,16 * * * python3 SEP_get_def.py"

"# Will run the script once a day at 15:15 every day"

"15 15 * * * python3 SEP_get_def.py"

"# Will run the script every hour and every day at 00:15, 01:15, 02:15..."

"15 * * * * python3 SEP_get_def.py"


