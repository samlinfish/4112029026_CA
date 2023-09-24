# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import time

os.mkdir('CS')

file = open("CS/homework.txt","w")
file.write('4112029026_林弘宇')
file.close()

file = open("CS/homework.txt","r")
content = file.read()
print(content)
file.close()

file_size = os.path.getsize('C:/Users/USER/.spyder-py3/CS/homework.txt')
print(f'文件大小:{file_size}字節')

mod_time = os.path.getmtime('C:/Users/USER/.spyder-py3/CS/homework.txt')
print(f'最後修改時間:{mod_time}')

formatted_time = time.ctime(mod_time)
print(f'最後修改時間(人類可讀格式):{formatted_time}')

os.remove("C:/Users/USER/.spyder-py3/CS/homework.txt")
os.rmdir("C:/Users/USER/.spyder-py3/CS")