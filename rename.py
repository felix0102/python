#!/usr/bin/env python3
import os
from urllib.request import quote


rootdir = '/Users/xianfliu/SDrive/www/wiki/data/pages'

img_file_l = []
img_dir_l = []

for parent, dirnames, filenames in os.walk(rootdir):
    for img_one in filenames:
        new_name = img_one.replace(".md", ".txt") 
        new_name = os.path.join(parent, new_name)
        old_name = os.path.join(parent, img_one)
        print(old_name)

        #new_name = quote(old_name, safe=";/?:@&=+$,", encoding="utf-8")
        #print(new_name)
        
        #sed_str="sed -i '' '1,9d' '" + old_name+"'";
        #print(sed_str)
        #os.popen(sed_str)
        os.rename(old_name, new_name)


