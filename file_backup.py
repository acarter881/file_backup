#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
from os import walk

src = "/home/student-00-01fd3438ab09/data/prod/"
dest = "/home/student-00-01fd3438ab09/data/prod_backup/"

def backup_data(dir):
  subprocess.call(["rsync", "-arq", src+dir, dest+dir])

if __name__ == '__main__':
  dir_list = []
  for (root, dirs, files) in walk(src):
    dir_list.extend(dirs)
    break
  p = Pool(len(dir_list))
  p.map(backup_data, dir_list)
