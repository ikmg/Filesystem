import platform
import subprocess
from abc import abstractmethod, ABC

from ._path_ import Path
from ._name_ import Name
from ._size_ import Size


class ObjectOS(ABC):

    def __init__(self, path: str):
        self.path = Path(path)
        self.name = Name(self.path.absolute)
        self.size = self.get_size()

    def __repr__(self):
        return '<{}>'.format(self.path.absolute)

    def open(self):
        """
        Открытие объекта средствами операционной системы
        """
        if self.path.is_exists:
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
        """
        Абстрактный метод копирования себя как объекта операционной системы
        в новый объект операционной системы, должен возвращать объект операционной системы
        """
        pass

    @abstractmethod
    def remove(self) -> None:
        """
        Абстрактный метод удаления себя как объекта операционной системы
        """
        pass

    def move(self, destination: str):
        """
        Перемещение себя как объекта операционной системы.
        Последовательное копирование и удаление.
        Возвращает объект операционной системы.
        """
        object_os = self.copy(destination)
        self.remove()
        return object_os

    @abstractmethod
    def get_size(self) -> Size:
        """
        Абстрактный метод вычисления размера объекта операционной системы
        """
        pass
