import os
import platform


def check_path(path: str) -> None:
    """
    Проверка значения параметра path на принадлежность к классу str
    """
    if not isinstance(path, str):
        raise ValueError('path <{}> must be string'.format(path))


def convert_path(path: str) -> str:
    """
    Приведение значения path к формату операционной системы
    """
    if platform.system() == 'Windows' and '/' in path:
        # Windows
        return path.replace('/', '\\')
    elif '\\' in path:
        # Linux, MacOS
        return path.replace('\\', '/')
    else:
        return path


def join_path(parent: str, child: str):
    return os.path.join(parent, child)


def list_dir(path: str):
    return [join_path(path, i) for i in sorted(os.listdir(path))]


def file_size(path: str):
    return os.path.getsize(path)


def dir_size(path: str):
    size = file_size(path)
    content = list_dir(path)
    for item in content:
        size += get_size(item)
    return size


def get_size(path: str):
    if os.path.isdir(path):
        size = dir_size(path)
    else:
        size = file_size(path)
    return size
