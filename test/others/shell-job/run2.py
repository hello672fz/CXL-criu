#!/usr/bin/env python
import os, pty, sys, subprocess
cr_bin = "../../../criu/criu"

os.chdir(os.getcwd())

if not os.access("work", os.X_OK):
    os.mkdir("work", 0o755)

open("running", "w").close()
pid = 4329

cmd = [cr_bin, "dump", "-j", "-t", str(pid), "-D", "work", "-v"]
print("Run: %s" % " ".join(cmd))
ret = subprocess.Popen(cmd).wait()
if ret != 0:
    sys.exit(1)

