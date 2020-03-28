
from multiprocessing import Pool
import multiprocessing
import subprocess
import os

src = "prod/"
dest =  "prod_backup/"

if __name__ == "__main__":
  pool = Pool(multiprocessing.cpu_count())
  pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))
