import sys

# you can write to stderr for debugging purposes, e.g.
# sys.stderr.write("this is a debug message\n")
# +6b25 +50 -2b25 +10b20 -50

def loadunload(load):
    if 'b' in load:
        load = load.split("b")
        boxes = int(load[0])
        pounds = int(load[1])
        totalweight = (boxes * pounds)
        output = str(totalweight)
        return(output)
    else:
        totalweight = int(load)
        output = str(totalweight)
        return(output)

def main():
    load = ""
    # write your code in Python 3.6
    totalweight = loadunload(load)
    print(totalweight)
    sys.stderr.write(loadunload(load))
    
if __name__ == '__main__':
    main()