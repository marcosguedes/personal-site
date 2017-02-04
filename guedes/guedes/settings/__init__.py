import os.path
import glob
conffiles = glob.glob(os.path.join(os.path.dirname(__file__), '*.conf.py'))
conffiles.sort()
for f in conffiles:
    # execfile(os.path.abspath(f))
    # print(f)
    exec(open(f).read())
