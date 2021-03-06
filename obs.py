import subprocess, os, datetime, time

try:
	obspath = open("obspath").read()
	print("OBS location:", obspath)
	path, file = os.path.split(obspath) # obspath contains the OBS executable's path as string
except:
	print("Error: could not parse OBS path")
	exit()
	
os.chdir(path) # switch to obs
dtNow = datetime.datetime.now()
timestring = input("starting time dd.mm.yy HH:MM (eg. 06.03.21 00:53):")
dtStart = datetime.datetime.strptime(timestring, "%d.%m.%y %H:%M")
dtDelta = dtStart - dtNow;
waittime = dtDelta.total_seconds();
if waittime < 0:
	print("Error: start in past")
	exit()
	
print("starting recording at", timestring, "in", waittime / 3600, "hours (", waittime / 60, " minutes)")
time.sleep(waittime)
subprocess.run(file + " --startrecording --minimize-to-tray --verbose", shell=True)

