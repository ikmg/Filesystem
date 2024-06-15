import os
import shutil

from ._path_ import check_on_str
from ._name_ import DirName
from ._size_ import Size
from ._object_ import ObjectOS
from .file import File


class Directory(ObjectOS):
    """
    Директория операционной системы
    """

    def __init__(self, path: str):
        super().__init__(path)
        self.name = DirName(self.path.absolute)
        if self.path.is_exists and not os.path.isdir(self.path.absolute):
            raise ValueError('path <{}> is not a directory'.format(self.path.absolute))

    def copy(self, destination: str):
        return copy_dir(self, destination)

    def remove(self) -> None:
        if self.path.is_exists:
            shutil.rmtree(self.path.absolute)

    def get_size(self) -> Size:
        """
        Размер директории в байтах.
        """
        if not self.path.is_exists:
            return Size(0)
        size = os.path.getsize(self.path.absolute)  # сама директория тоже весит
        children = self.child_list()  # список дочерних элементов директории
        for child_path in children:  # рекурсивный перебор дочерних элементов
            if os.path.isdir(child_path):  # директория
                size += Directory(child_path).size.b
            elif os.path.isfile(child_path):  # файл
                size += File(child_path).size.b
        return Size(size)

    def create(self) -> None:
        """
        Создание директории (самой себя) если она не присутствует в операционной системе
        """
        parent_dir = self.path.parent()
        if parent_dir.is_exists:
            if not self.path.is_exists:
                os.mkdir(self.path.absolute)
        else:
            raise FileExistsError('parent directory <{}> is not exists'.format(parent_dir.absolute))

    def join(self, child: str) -> str:
        """
        Добавление дочернего элемента
        """
        check_on_str(child)
        return os.path.join(self.path.absolute, child)

    def child_list(self) -> list:
        return list_dir(self)

    def child_dirs(self) -> list:
        """
        Список дочерних директорий объектов класса Directory
        """
        result = []
        for child_path in self.child_list():
            if os.path.isdir(child_path):
                result.append(Directory(child_path))
        return result

    def child_files(self) -> list:
        """
        Список дочерних файлов объектов класса File
        """
        result = []
        for child_path in self.child_list():
            if os.path.isfile(child_path):
                result.append(File(child_path))
        return result


def copy_dir(source: Directory, destination: str) -> Directory:
    """
    Копирование директории
    """
    check_on_str(destination)
    if source.path.is_exists:
        new_dir = Directory(destination)
        if not new_dir.path.is_exists:
            parent_dir = new_dir.path.parent()
            if parent_dir.is_exists:
                shutil.copytree(
                    src=source.path.absolute,
                    dst=new_dir.path.absolute,
                    symlinks=False,
                    ignore_dangling_symlinks=True
                )
                return new_dir
            else:
                raise IsADirectoryError('destination path <{}> is not exists'.format(parent_dir.path.absolute))
        else:
            raise SystemError('destination directory <{}> is already exists'.format(new_dir.path.absolute))
    else:
        raise FileExistsError('source directory <{}> is not exists'.format(source.path.absolute))


def list_dir(directory: Directory):
    """
    Список дочерних элементов, существующих в операционной системе
    """
    if directory.path.is_exists:
        return [directory.join(i) for i in sorted(os.listdir(directory.path.absolute))]
    else:
        raise IsADirectoryError('directory path <{}> is not exists'.format(directory.path.absolute))


