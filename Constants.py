with open('E:\\DIRS.txt','r') as f:
    content = f.readlines()
    _ROOT_DIR = content[0][:-1] # slicing to remove '\n'
    _MAIN_DIR = content[1]

