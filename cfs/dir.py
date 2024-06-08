import os

from .file import File
from .object import Object
from .tools import check_path, list_dir, join_path


class Dir(Object):
    """
    Директория операционной системы
    """

    def __init__(self, path: str):
        super().__init__(path)
        if self.is_exists and not os.path.isdir(self.path.absolute):
            raise ValueError('path <{}> is not a directory'.format(self.path.absolute))

    def create(self) -> None:
        """
        Создание директории (самой себя) если она не присутствует в операционной системе
        """
        if self.is_parents_exists:
            if not self.is_exists:
                os.mkdir(self.path.absolute)
        else:
            raise FileExistsError('parent directory <{}> is not exists'.format(self.parent.path))

    def join(self, child: str):
        """
        Добавление дочернего элемента
        """
        check_path(child)
        return join_path(self.path.absolute, child)

    def children(self):
        """
        Список дочерних элементов, существующих в операционной системе
        """
        if self.is_exists:
            return list_dir(self.path.absolute)
        return None

    def child_dirs(self):
        result = []
        if not self.is_exists:
            return result

        for child_path in self.children():
            if os.path.isdir(child_path):
                result.append(Dir(child_path))
        return result

    def child_files(self):
        result = []
        if not self.is_exists:
            return result

        for child_path in self.children():
            if os.path.isfile(child_path):
                result.append(File(child_path))
        return result

    def copy(self, destination: str):
        # TODO
        pass

    def remove(self):
        # TODO
        pass
