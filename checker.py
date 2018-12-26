import subprocess
import argparse
import os

cwd = os.path.dirname(__file__)

PYTHON_CMD = ["python3",cwd + "/target/python3/main.py"]
NODE_CMD = ["node",cwd + "/target/node8/main.js"]
JAVA_COMPILE_CMD = ["javac",cwd + "/target/java8/Main.java"]
JAVA_EXE_COM = ["java", "-cp", cwd + "/target/java8", "Main"]

def execute_test(cmd,path,file):
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)
    with open(path + "test/" + file) as f:
        out = proc.communicate(f.read().encode())[0].decode()
        with open(path  + "answer/" + file) as ansf:
            ans = ansf.read()
            print('##' + file + '##')
            print(out == ans)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("question")
    parser.add_argument("lang")
    
    args = parser.parse_args()
    
    
    if(args.lang == "java"):
        subprocess.call(JAVA_COMPILE_CMD)
        cmd = JAVA_EXE_COM

    else:
        cmd = NODE_CMD if args.lang == "node" else PYTHON_CMD


    
    path = cwd + "/questions/" + args.question + "/"
    
    for(root, dir, files) in os.walk(path + "test/"):
        for file in files:
            execute_test(cmd,path,file)