import os
from collections import defaultdict

def main(argv):
    programm,*args = argv
    limit_data = [10 ** item for item in range(1, 20)]
    curr_dir = args[0]
    def_dict = dict()

    for root, dirs, files in os.walk(curr_dir):
        for file in files:
            for data in limit_data:
                file_size =  os.stat(os.path.join(root,file)).st_size
                if file_size <= data:
                    if not data in def_dict:
                        def_dict[data] = 1
                    else:
                        def_dict[data] += 1
                    break;

    print(def_dict)


if __name__=='__main__':
    import sys
    exit(main(sys.argv))