import os
import shutil
import hashlib

from .object import Object
from .tools import check_path


class File(Object):
    """
    Файл операционной системы
    """

    def __init__(self, path: str):
        super().__init__(path)
        if self.is_exists and not os.path.isfile(self.path.absolute):
            raise ValueError('path <{}> is not a file'.format(self.path.absolute))

    def copy(self, destination: str):
        """
        Копирование файла
        """
        check_path(destination)
        if self.is_exists:
            new_file = File(destination)
            if not new_file.is_exists:
                if new_file.is_parents_exists():
                    shutil.copyfile(self.path.absolute, destination)
                    return new_file
                else:
                    raise IsADirectoryError('destination <{}> is not exists'.format(new_file.parent.path.absolute))
            else:
                raise SystemError('file <{}> is already exists'.format(new_file.path.absolute))
        else:
            raise FileExistsError('file <{}> is not exists'.format(self.path.absolute))

    def remove(self):
        """
        Удаление файла
        """
        os.remove(self.path.absolute)

    def md5(self) -> str:
        """
        Хэш-сумма файла
        """
        with open(self.path.absolute, 'rb') as f:
            m = hashlib.md5()
            while True:
                data = f.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()
