import os
from os import walk
import shutil

baseDirectory = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')


source = baseDirectory+'/Shard_Source/'

dest = baseDirectory+'/Shard_Dest/'

print (source)

for (dirpath, dirnames, filenames) in walk(source):
    for f in filenames:
        first_three = f[:3]
        directory_list = list(first_three)
        first_level = directory_list[0].lower()
        second_level = directory_list[1].lower()
        third_level = directory_list[2].lower()

        directory_name ='/'+first_level+'/'+second_level+'/' + third_level + '/'

        if not os.path.isdir(dest+directory_name):
            os.makedirs(dest+directory_name)

        shutil.move(source+f, dest+directory_name)
    break
