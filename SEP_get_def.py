""""
  Access Symantec definitions website to get links to definitions installers
  (x32 and x64) and than download the files to a specific directory at a specifc
  server.
  Attention!!!!
  The directory must be defined in the "path" variable. If don't it will clear
  the current directory.

  It's Python 3!!!

  André das Neves
  ansone [at] g[oogle]mail [dot] com
"""
import os
import platform
import urllib.request as wget
import time
from datetime import date
from datetime import datetime

# Clean screen
os.system('cls' if os.name == 'nt' else 'clear')

# platform.system is a newer and better implemented module than os.name
system_OS = platform.system()
if system_OS=='Linux':
    import pwd
    import grp
    path = "/home/serpro/fileserver/_instalacao/Antivirus/Atualização"
    user_name = 'serpro'
    group_name = 'serpro'
elif system_OS=='Windows':
    path = "C:\\Users\\Dexter\\Downloads\\Teste"
else:
    print("How stupid is someone using a Mac Server?")
print("Are you a {} user?".format(system_OS))

today = datetime.now()
print("Starting job: {}.".format(datetime.now().strftime("%d/%h/%Y %H:%M")))

# Changing current directory
if(os.path.isdir(path)):
    os.chdir(path)
    current = os.getcwd();
    # Verifying the current working path
    if path == current:
        # Get webpage html file
        fp = wget.urlopen("http://www.symantec.com/security_response/definitions/download/detail.jsp?gid=sep")
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()

    # Catching links from webpage
        # Link to x32
        a = mystr.find("http://definitions.symantec.com/defs/")
        b = mystr.find("\"", a)
        link1 = mystr[a:b]
#        print(link1)
        filename1 = link1.rsplit('/',1)[1]

        # Link to x64
        c = mystr.find("http://definitions.symantec.com/defs/", b)
        d = mystr.find("\"", c)
        link2 = mystr[c:d]
#        print(link2)
        filename2 = link2.rsplit('/',1)[1]

        # Download x32 installer
        if not os.path.exists(filename1):
            print("File {} not found. Take a break while I download it.".format(filename1))
            start_time = time.time()
            wget.urlretrieve(link1, filename1)
            elapsed_time = time.time()-start_time
            file_info = os.stat(filename1)
            print("{0:.1f} sec to download it.".format(elapsed_time))
            print("Dowload speed: {0:.1f} kB/sec.".format(file_info.st_size/elapsed_time/1000000))
            with open("SEP_get_def.log", "a") as log:
                log.write("{} New definitions found. File {} have been downloaded.\n".format(datetime.now().strftime("%Y%m%d-%H%M"), filename1))
        else:
            print("{} file already exists. I'm too lazy to do it again.".format(filename1))
            with open("SEP_get_def.log", "a") as log:
                log.write("{} No definitions found. File {} already downloaded.\n".format(datetime.now().strftime("%Y%m%d-%H%M"), filename1))
        # Download x64 installer
        if not os.path.isfile(filename2):
            print("File {} not found. Take a break while I download it.".format(filename2))
            start_time = time.time()
            wget.urlretrieve(link2, filename2)
            elapsed_time = time.time()-start_time
            file_info = os.stat(filename2)
            print("{0:.1f} sec to download it".format(elapsed_time))
            print("Dowload speed: {0:.1f} kB/sec".format(file_info.st_size/elapsed_time/1000000))
            with open("SEP_get_def.log", "a") as log:
                log.write("{} New definitions found. File {} have been downloaded.\n".format(datetime.now().strftime("%Y%m%d-%H%M"), filename2))
        else:
            print("{} file already exists. I will sleep for a while.".format(filename2))
            with open("SEP_get_def.log", "a") as log:
                log.write("{} No definitions found. File {} already downloaded.\n".format(datetime.now().strftime("%Y%m%d-%H%M"), filename2))

        # Remove older definitions installers versions
        print("\nCleaning the old mess...:\n")
        for f in os.listdir(path):
            if((f!=filename1) & (f!=filename2) & (f!="SEP_get_def.log") & (f!="SEP_get_def.py")):
                os.unlink(f)
                print('{} removed'.format(f))

        # Change file permissions on linux systems
        if system_OS=='Linux':
            uid = pwd.getpwnam(user_name).pw_uid
            gid = grp.getgrnam(group_name).gr_gid
            for f in os.listdir(path):
                os.chown(f, uid, gid)
    else:
        print("Not the right directory. Better run away!")
else:
    print("Path is not a directory or doesn't really exists. Can't help you with that. Loser!")
