import platform
import subprocess
from abc import abstractmethod

from .path import Path
from .tools import get_size


def is_parents_exists(obj: Path):
    """
    Проверка существования в операционной системе всех родительских директорий
    """
    if obj.parent:  # если у объекта есть родительская директория
        if obj.parent.is_exists:  # если родительская директория существует
            return is_parents_exists(obj.parent)  # рекурсия
        else:
            return False  # путь не валидный
    else:  # если у объекта нет родительской директории, то это корень системы
        return True


class Size:

    def __init__(self, path: str):
        self.b = get_size(path)
        self.kb = round(self.b / 1024, 2)
        self.mb = round(self.kb / 1024, 2)
        self.gb = round(self.mb / 1024, 2)

    def __repr__(self):
        if self.gb > 1:
            return '<{} GB ({} b)>'.format(self.gb, self.b)
        elif self.mb > 1:
            return '<{} MB ({} b)>'.format(self.mb, self.b)
        elif self.kb > 1:
            return '<{} KB ({} b)>'.format(self.kb, self.b)
        else:
            return '<{} b>'.format(self.b)


class Object(Path):

    def __init__(self, path: str):
        super().__init__(path)
        self.is_parents_exists = is_parents_exists(self)

    def size(self):
        return Size(self.path.absolute)

    def open(self) -> None:
        """
        Открытие объекта средствами операционной системы
        """
        if self.is_exists:
            if platform.system() == 'Darwin':  # MacOS
                subprocess.call(('open', self.path.absolute))
            elif platform.system() == 'Windows':  # Windows
                subprocess.call(('start', "", self.path.absolute), shell=True)
            else:  # Linux
                subprocess.run(['xdg-open', self.path.absolute])
        else:
            raise FileExistsError('object <{}> is not exists'.format(self.path.absolute))

    @abstractmethod
    def copy(self, destination: str):
        pass

    @abstractmethod
    def remove(self):
        pass

    def move(self, destination: str):
        new_obj = self.copy(destination)
        self.remove()
        return new_obj
