import os

process = "sshd"

strem = os.popen(f"ps -ef | grep {process} | grep -v grep | wc -l")
strem = int(strem.read().strip())

if strem > 0:

    print("Process is running")

else:

    print("please check !, process is not running")
