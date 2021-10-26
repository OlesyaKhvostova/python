import os

project_struct = {'my_project':{'settings':{},'mainapp':{},'adminapp':{},'authapp':{}}}


def create_folders(parent_obj, child):
    for key,value in child.items():
        folder_base = os.path.join(parent_obj,key)
        if not os.path.exists(folder_base):
            os.makedirs(folder_base)
        create_folders(folder_base,value)

with open('config.yaml','w',encoding='utf-8') as config_file:
    config_file.write(str(project_struct))

create_folders('',project_struct)