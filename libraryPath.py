import os 

def libraryPath(path):
    download_folder_path = path
    path = os.getcwd()+"/{folder}".format(folder= download_folder_path)
    # print(path)
    return path

# libraryPath("video-library")