# This code install line by line a list of pip package
import sys
import pip

def install(package):
    pip.main(['install', package])

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            install(line)