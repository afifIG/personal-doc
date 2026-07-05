import os
 

#  lebel means and the comment's that is called labls
#  Specify the diroctory Path
path = "."

# print all files and folders in the dicrectory
contents = os.listdir(path)
 

# print all items in the directory foder.
for item in contents:
    print(item)