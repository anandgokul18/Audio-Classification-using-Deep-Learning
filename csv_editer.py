import os
import shutil

import os.path
from os import path
import pandas as pd

#allfiles_dir = os.path.join(os.getcwd(),'sounds','train','train_sound')    # Directory to move images from

df1 = pd.read_csv("/home/anandgokul18/audio/sounds/labels/train.csv")

print(df1.head())
import pdb
pdb.set_trace()

#target_ext = 'wav'                                  # File extension/type (used to filter input images)

#_, _, file_names = next(os.walk(allfiles_dir))       # Get all image names

for index, row in df1.iterrows():
   if path.exists(row['ID']):
      pass
   else:
      df1.drop(index , inplace=True)

'''
for name in file_names:
    # Ignore hidden files and non matching file extensions (target_ext)
   if name[0] != '.' and name.split('.')[1] == target_ext:
         #shutil.move(os.path.join(allfiles_dir, name), os.path.join(target_dir, name))
         indexNames = data[ data['ID'] == 30 ].index
'''