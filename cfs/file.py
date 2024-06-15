import hashlib
import os
import shutil

from ._path_ import check_on_str
from ._name_ import FileName
from ._size_ import Size
from ._object_ import ObjectOS


class File(ObjectOS):
    """
    Файл операционной системы
    """

    def __init__(self, path: str):
        super().__init__(path)
        self.name = FileName(self.path.absolute)
        if self.path.is_exists and not os.path.isfile(self.path.absolute):
            raise ValueError('path <{}> is not a file'.format(self.path.absolute))

    def copy(self, destination: str):
        return copy_file(self, destination)

    def remove(self) -> None:
        if self.path.is_exists:
            os.remove(self.path.absolute)

    def get_size(self) -> Size:
        """
        Размер файла в байтах
        """
        if not self.path.is_exists:
            return Size(0)
        size = os.path.getsize(self.path.absolute)
        return Size(size)

    def md5(self) -> str:
        """
        Хэш-сумма файла
        """
        if self.path.is_exists:
            with open(self.path.absolute, 'rb') as f:
                m = hashlib.md5()
                while True:
                    data = f.read(8192)
                    if not data:
                        break
                    m.update(data)
                return m.hexdigest()
        else:
            raise FileExistsError('file <{}> is not exists'.format(self.path.absolute))


def copy_file(source: File, destination: str) -> File:
    """
    Копирование файла
    """
    check_on_str(destination)
    if source.path.is_exists:
        new_file = File(destination)
        if not new_file.path.is_exists:
            parent_dir = new_file.path.parent()
            if parent_dir.is_exists:
                shutil.copyfile(source.path.absolute, new_file.path.absolute)
                return new_file
            else:
                raise IsADirectoryError('destination path <{}> is not exists'.format(parent_dir.path.absolute))
        else:
            raise SystemError('destination file <{}> is already exists'.format(new_file.path.absolute))
    else:
        raise FileExistsError('source file <{}> is not exists'.format(source.path.absolute))
