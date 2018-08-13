#
#start firefox or switch to firefox
import subprocess
command = 'wmctrl -l'
output = system.exec_command(command, getOutput=True)

if 'code' in output:
    window.activate('code' ,switchDesktop=True)

else:
    subprocess.Popen(["/usr/bin/code"])
#