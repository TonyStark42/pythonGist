from pathlib import Path

def count_lines(paths):
    acc = 0
    for p in paths:
        filecount = getFileLineCount(p)
        acc += filecount
    return acc  


def getFileLineCount(file):
    count = 0
    try:
        thefile = open(file)
        while 1:
            buffer = thefile.read(65536)
            if not buffer: break
            count += buffer.count('\n')
    except:
        print("error reading file")
    return count

path = "C:/code" 
paths = Path(path).glob("**/*.cs")  
count =count_lines(paths)
print(count)

