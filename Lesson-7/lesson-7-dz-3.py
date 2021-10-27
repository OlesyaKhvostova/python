import os


def get_template_folders():
    target_path = []
    for root, dirs, files in os.walk('my_project'):
        for dir in dirs:
            if dir == 'templates':
                target_path.append(os.path.join(root, dir))

    return target_path


target_path = get_template_folders()
path_target = 'my_project\\templates'

if not os.path.exists(path_target):
    os.makedirs(path_target)
if path_target in target_path:
    target_path.remove(path_target)

for dir in target_path:
    for item in os.scandir(dir):
        to_path = os.path.join(path_target, item.name)
        from_path = os.path.join(dir, item.name)
        os.rename(from_path, to_path)
