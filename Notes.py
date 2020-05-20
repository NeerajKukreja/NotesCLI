#!C:\Users\admin\Anaconda3 python
import argparse
import os
import sys


def newFile(args,_MAIN_DIR,_ROOT_DIR):
    filename = args.NewFile[0]
    filepath = _MAIN_DIR + '\\' + filename
    with open(filepath,'w') as f:
        pass
    
def readFile(args,_MAIN_DIR,_ROOT_DIR):
    filename = args.read[0]
    filepath = _MAIN_DIR + '\\' + filename
    os.system('start ' + filepath)

def mkdir(args,_MAIN_DIR,_ROOT_DIR):
    dirname = args.newdir[0]
    path = _MAIN_DIR + '\\' + dirname
    try:
        os.mkdir(path)
        print(f"{dirname} directory created")
    except Exception as e:
        print(e)

def changedir(args,_MAIN_DIR,_ROOT_DIR):
    dirname = args.change[0]
    if _MAIN_DIR != _ROOT_DIR + '\\\\' + dirname: 
        _MAIN_DIR = _ROOT_DIR + '\\\\' + dirname
        with open(f'E:\\DIRS.txt','w') as f:
            f.writelines([_ROOT_DIR+'\n', _MAIN_DIR])
        print('Directory changed to',_MAIN_DIR)
    else:
        print('You are in the directory!')

def resetdir(args,_MAIN_DIR,_ROOT_DIR):
    _MAIN_DIR = _ROOT_DIR
    with open(f'E:\\DIRS.txt','w') as f:
            f.writelines([_ROOT_DIR+'\n', _MAIN_DIR])

def listdir(args,_MAIN_DIR):
    for d in os.listdir(_MAIN_DIR):
        print(d)

def configure(args):
    directory = args.config[0]
    if not os.path.exists(directory):
        os.mkdir(directory)
    with open(f'E:\\DIRS.txt','w') as f:
        f.writelines([directory+'\n', directory])

# Main
if __name__ == '__main__':
    #TODO: ADD config commands..

    parser = argparse.ArgumentParser(description= 'Makes Notes')

    # Adding config command:
    parser.add_argument('--config', nargs=1, metavar="directory", type=str, help="sets default directory")
    # Create a new file
    parser.add_argument('-nf','--NewFile',nargs=1, metavar="filename", type=str, help="creates a new file")
    # Opens a file with standard application
    parser.add_argument('-rf','--read', nargs=1, metavar="filename", type=str, help="Opens a file")
    # Create a directory:
    parser.add_argument('-nd', '--newdir', nargs=1, metavar="Dir name", type=str, help="Create a dir under Notes folder")
    # Change the working directory:
    parser.add_argument('-cd', '--change', nargs=1, metavar="dir name", type=str, help="change directory")
    # Reset Directory
    parser.add_argument('-rd', '--reset', nargs=1, metavar='1 to reset', type=int, help="key = 1 resets directory")
    # Lists all files in a cd:
    parser.add_argument('-ls','--list', nargs=1, metavar='1 to list', type=int, help='key = 1 lists')


    args = parser.parse_args()
    if args.config!=None:
        configure(args)
    else:
        import Constants as c
        if args.NewFile!=None:
            newFile(args,c._MAIN_DIR,c._ROOT_DIR)
        elif args.read!=None:
            readFile(args,c._MAIN_DIR,c._ROOT_DIR)
        elif args.newdir!=None:
            mkdir(args,c._MAIN_DIR,c._ROOT_DIR)
        elif args.change!=None:
            changedir(args,c._MAIN_DIR,c._ROOT_DIR)
        elif args.reset!=None:
            if args.reset[0] == 1:
                resetdir(args,c._MAIN_DIR,c._ROOT_DIR)
        elif args.list!=None:
            if args.list[0] == 1:
                listdir(args,c._MAIN_DIR)