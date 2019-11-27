import os
import shutil

allfiles_dir = os.path.join(os.getcwd(),'sounds','train','train_sound')    # Directory to move images from
target_dir1 = os.path.join(os.getcwd(),'sounds','train','model1')       # Directory to move images onto
target_dir2 = os.path.join(os.getcwd(),'sounds','train','model2')       # Directory to move images onto
target_dir3 = os.path.join(os.getcwd(),'sounds','train','model3')       # Directory to move images onto


target_ext = 'wav'                                  # File extension/type (used to filter input images)

_, _, file_names = next(os.walk(allfiles_dir))       # Get all image names

count=0

for name in file_names:
    # Ignore hidden files and non matching file extensions (target_ext)
   if name[0] != '.' and name.split('.')[1] == target_ext:
      if count==0:
         shutil.copy(os.path.join(allfiles_dir, name), os.path.join(target_dir1, name))
      if count==1:
         shutil.copy(os.path.join(allfiles_dir, name), os.path.join(target_dir2, name))
      if count==2:
         shutil.copy(os.path.join(allfiles_dir, name), os.path.join(target_dir3, name))
   if count==2:
      count=0
   else:
      count+=1
