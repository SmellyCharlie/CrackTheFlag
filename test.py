from subprocess import *

def write(process, data):
    process.communicate(data)


def read(process):
    print(process.stdout)

def main():
    process = input
    p = run(process, stdin=PIPE, input=None, stdout=PIPE, stderr=STDOUT, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, env=None, universal_newlines=None)
    

if __name__ == '__main__':
    main()s