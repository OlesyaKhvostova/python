import os
import json

project_struct = {'my_project':{\
'settings':{'__init__.py':{}, 'dev.py':{}, 'prod.py':{}},\
'mainapp':{'__init__.py':{}, 'models.py':{}, 'views.py':{}, \
    'templates':{'mainapp':{'base.html':{}, 'index.html':{}}}},\
'authapp':{'__init__.py':{}, 'models.py':{}, 'views.py':{}, \
    'templates':{'authapp':{'base.html':{}, 'index.html':{}}}}}}


def create_folders(parent_obj, child):
    for key, value in child.items():
        ext = key.rsplit('.', maxsplit=1)[-1].lower()
        if (ext == key):
            ext = ''
        folder_base = os.path.join(parent_obj, key)
        if not os.path.exists(folder_base):
            if len(ext):
                curr_file = open(folder_base, 'x', encoding='utf-8')
                curr_file.close()
            else:
                os.makedirs(folder_base)

        if not len(ext):
            create_folders(folder_base, value)


with open('config.yaml','w',encoding='utf-8') as config_file:
    json.dump(project_struct, config_file)

with open('config.yaml','r',encoding='utf-8') as config_file:
    project_struct_temp = dict()
    project_struct_temp = json.load(config_file)

create_folders('',project_struct_temp)
