import glob
import os

'''
To remove website from all songs in a folder
ex: songdownloader-songname.mp3
'''

seperator='-' # seperator - or <space> <[,]>
path=r'/Users/uday/Desktop/songs/'#path to folder
files=glob.glob(os.path.join(path,'*')) 

for file in files:
    file_name=os.path.basename(file)
    if '-' in file_name:
        new_name=file_name.split(sep=seperator)[1].strip()

        print(new_name)
        new_full_path=os.path.join(path,new_name)
        current_full_path=os.path.join(path,file_name)
        os.rename(current_full_path,new_full_path)
