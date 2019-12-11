import os
import shutil

target_dir = os.path.join(os.getcwd(),'sounds','train','train_sound')    # Directory to move images from
allfiles_dir = os.path.join(os.getcwd(),'sounds','train','train_sound_activelearning_30')       # Directory to move images onto

target_ext = 'wav'                                  # File extension/type (used to filter input images)

_, _, file_names = next(os.walk(allfiles_dir))       # Get all image names

count=0

list1=[]

for name in file_names:
   
    # Ignore hidden files and non matching file extensions (target_ext)
   if name[0] != '.' and name.split('.')[1] == target_ext:
      list1.append(name)
   '''
       if count==7 or count==8 or count==9:
         #shutil.move(os.path.join(allfiles_dir, name), os.path.join(target_dir, name))
   if count==9:
      count=0
   else:
      count+=1
    '''

from random import sample
print(len(list1))

movelist=sample(list1,163)

print(len(movelist))
for name in movelist:
    #print(list1[0])
    shutil.move(os.path.join(allfiles_dir, name), os.path.join(target_dir, name))

