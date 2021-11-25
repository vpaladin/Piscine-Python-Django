import re
import sys  


def main(arg):
    path = re.findall(r'\w+\.template$', arg)
    if len(path) == 0:
        print("Arg need have .template")
        return
    with open(f"{arg}",'r') as f:
        data = f.read()
        for key,item in values.items():
            data = re.sub("{"+ key + "}", item, data)
    new_path = arg[:arg.rfind(".template")]
    with open(f"{new_path}.html", 'w') as f:    
        f.write(data)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open("settings.py", 'r') as f:
            values = {}
            line = f.readline()
            while (line):
                val = re.split(r'=', line)
                values[val[0][:-1]] = val[1].strip('\"\'\n ')
                line = f.readline()
        main(sys.argv[1])
    else:
        print("Not valid count arguments")