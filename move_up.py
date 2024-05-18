import sys
import os
import shutil

dir = sys.argv[1].replace("\\","\\\\")

parent_dir = dir.rsplit("\\\\",1)[0]
items = os.listdir(dir)

for item in items:
	src = os.path.join(dir, item)
	dest = os.path.join(parent_dir, item)
	shutil.move(src, dest)

shutil.rmtree(dir)