import os

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

    def copy(self, destination: str):
        pass

    def remove(self):
        pass
