
### Troubleshooting and Debugging Techniques
## Qwiklabs Assessment (Week 2): Performance Tuning in Python Scripts
# nano --tabsize ~/scripts/dailysync.py

from multiprocessing import Pool
import subprocess
import os

src = "/home/kgarbutt/Desktop/prod/"
dest = "/home/kgarbutt/Desktop/prod_backup/"

group = os.listdir(src)
# print(len(group))
print(group)

def main(task):
	for root, dirs, files in os.walk(src):
		subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
	p = Pool(len([dir for dirs in group]))
	p.map(main, group)


