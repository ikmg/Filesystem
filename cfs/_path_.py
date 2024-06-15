import os
import platform


def check_on_str(value) -> None:
    """
    Проверка параметра на принадлежность к классу str
    """
    if not isinstance(value, str):
        raise ValueError('path <{}> must be string'.format(value))


def convert_path(path: str) -> str:
    """
    Приведение значения path к формату операционной системы.
    Для кроссплатформенной работы необходимо подавать
    в качестве параметра относительный путь от рабочего каталога
    """

    # Если платформа относится к семейству Windows
    # и если в пути присутствует /
    # производится замена на \
    if platform.system() == 'Windows' and '/' in path:
        return path.replace('/', '\\')

    # В других случаях если в пути присутствует символ \
    # производится замена на /
    elif '\\' in path:
        return path.replace('\\', '/')

    # при отсутствии совпадений возвращается значение path
    else:
        return path


class Path:
    """
    Путь к объекту в операционной системе
    """

    def __init__(self, path: str):
        check_on_str(path)  # проверка значения
        self.absolute = os.path.abspath(convert_path(path))  # абсолютный путь
        self.relative = os.path.relpath(self.absolute)  # относительный путь

    def __repr__(self):
        return '<{}>'.format(self.absolute)

    @property
    def is_exists(self):
        return os.path.exists(self.absolute)

    def parent(self):
        """
        Родительская директория (Path)
        """
        parent = os.path.dirname(self.absolute)
        if parent == self.absolute:
            return None
        else:
            return Path(parent)

    def parts(self):
        """
        Составные части пути
        """
        separator = os.path.sep
        return [i for i in self.absolute.split(separator) if i]
