import os
import shutil

directory = r'C:\Users\benny\Scripts\OSI\src'
files = os.listdir(directory)
python_files = [file for file in files if file.endswith('.py')]

with open('all_code.py', 'wb') as outfile:
   for file in python_files:
       with open(os.path.join(directory, file), 'rb') as infile:
           shutil.copyfileobj(infile, outfile)
       outfile.write(b'\n')
