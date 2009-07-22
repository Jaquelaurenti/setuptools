import urllib2
import sys
import os

print '**** Starting Test'
print '\n\n'

is_jython = sys.platform.startswith('java')
if is_jython:
    import subprocess

print 'Downloading bootstrap'
file = urllib2.urlopen('http://nightly.ziade.org/bootstrap.py')
f = open('bootstrap.py', 'w')
f.write(file.read())
f.close()

# running it
args = [sys.executable]  + ['bootstrap.py']
if is_jython:
    subprocess.Popen([sys.executable] + args).wait()
else:
    os.spawnv(os.P_WAIT, sys.executable, args)

# now checking if Distribute is installed

args = [sys.executable]  + ['-c', 'import setuptools; import sys; sys.exit(hasattr(setuptools, "_distribute"))']
if is_jython:
    res = subprocess.call([sys.executable] + args)
else:
    res = os.spawnv(os.P_WAIT, sys.executable, args)

print '\n\n'
if res:
    print '**** Test is OK'
else:
    print '**** Test failed, please send me the output at tarek@ziade.org'

