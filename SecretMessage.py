import os
def rename_files(directory):
    file_list=os.listdir(directory)
    os.chdir(directory)
    for file in  file_list:
        os.rename(file,file.translate(None,"0123456789"))
        print file





rename_files("/home/mohamed97/Downloads/prank/prank")