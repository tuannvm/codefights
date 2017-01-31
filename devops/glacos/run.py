# 1. read start.hint, filter out the instructions (OK)
# copy them to list or dict (OK)
# check whether file or directory?
# if dir, then loop through the list and execute the correlative instruction
# end of list, looking for new unique hint file

import os

PATH = "/Users/tuannvm/codefights/devops/glacos/root/devops/cloud"
instructionList = []

def check_dir(path):
    return os.path.isdir(path)

def current_dir():
    return os.getcwd()

def list_dir(path):
    return os.listdir(path)

def get_parent_dir(path):
    return os.path.dirname(path)

def cd_dir(path):
    return os.chdir(path)

def read_file(filepath="start.hint"):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    if lines[0].strip("\n") == "Hint":
        return lines[1].strip("\n").split(" ")
    return False

def execution(directory, instruction):
    if instruction == "down":
        cd_dir(directory)
    if instruction == "up":
        cd_dir(get_parent_dir(current_dir()))


def get_sub_dirs(currentDir):
    subDirs = []
    directories = [f for f in os.listdir(currentDir) if os.path.isdir(f)]
    for directory in directories:
        for root, subdirs, files in os.walk(directory):
            subDirs.append(root.split('/'))
    return subDirs

def join_dir(subDirs, steps):
    matchDir = []
    for subDir in subDirs:
        if len(subDir) == steps:
            matchDir.append("/".join(subDir))
    return matchDir

def check_file_exists(currentDir):
    files = [f for f in os.listdir(currentDir) if os.path.isfile(f)]
    if len(files) != 0:
        return True
    return False


def get_hint_file(currentDir):
    files = [f for f in os.listdir(currentDir) if os.path.isfile(f)]
    try:
        files.remove("passed.txt")
    except ValueError:
        pass
    i = 0
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            if lines[0].strip("\n") == "Hint":
                i = i + 1
            #else:
                #files.remove(file)
    if i == 1:
        for file in files:
            with open(file, 'r') as f:
                lines = f.readlines()
                if lines[0].strip("\n") == "Hint":
                    return lines[1].strip("\n").split(" ")

def dir_is_valid(length, dirPath):
    if len(dirPath) >= length:
        #print "dir valid: " + str(dirPath)
        return True
    return False

def check_final_path(currentDir):
    files = [f for f in os.listdir(currentDir) if os.path.isfile(f)]
    for file in files:
        if file == "passed.txt":
            return True

def main_func(instructionList, subDirs, path):
    if instructionList == ['']:
        print current_dir()[1:]
        return True
    #print "********************************"
    #print subDirs
    #print path
    #print "step ###" + str(instructionList)
    currentDirs = []

    if len(subDirs) == 0:
        os.chdir(path)
        for i in range(0, len(instructionList)):
            if instructionList[i] == "down":
                main_func(instructionList[i:], get_sub_dirs(current_dir()), current_dir())
            if instructionList[i] == "up":
                os.chdir("..")


    for subDir in subDirs:
        os.chdir(path)
        if instructionList is None:
            continue
        try:
            for i in range(0, len(instructionList)):
                #print subDir
                if instructionList[i] == "down":
                    os.chdir(subDir[i])
                if instructionList[i] == "up":
                    os.chdir("..")
        except IndexError:
            continue
        except OSError:
            continue
        if get_hint_file(current_dir()):
            currentDirs.append(current_dir())

    currentDirs = list(set(currentDirs))
    for currentDir in currentDirs:
        if str(currentDir) == PATH:
            currentDirs.remove(currentDir)
    if len(currentDirs) == 0:
        return path
    os.chdir(str(currentDirs[0]))
    if check_final_path(current_dir()):
        print current_dir()[1:]
        return True
    fo = open("passed.txt", "wb")
    fo.close()

    #print current_dir()
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    if len(files) != 0:

        main_func(get_hint_file(current_dir()), get_sub_dirs(current_dir()), current_dir())

cd_dir(PATH)

dirList = list_dir(current_dir())
instructionList = get_hint_file(current_dir())
subDirs = get_sub_dirs(current_dir())

if instructionList is None:
    print current_dir()[1:]

main_func(get_hint_file(current_dir()), get_sub_dirs(current_dir()), PATH)
