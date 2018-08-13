#
#RUN Chrome
import subprocess
command = 'wmctrl -l'
output = system.exec_command(command, getOutput=True)

if 'Chrome' in output:
    window.activate('Chrome' ,switchDesktop=True)

else:
    subprocess.Popen(["/usr/bin/google-chrome"])
#