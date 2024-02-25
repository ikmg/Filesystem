import os

from .tools import check_path, convert_path


class Base:

    def __init__(self, path: str):
        check_path(path)
        self.absolute = os.path.abspath(convert_path(path))  # абсолютный путь
        self.relative = os.path.relpath(self.absolute)  # относительный путь

    def __repr__(self):
        return '<{}>'.format(self.absolute)


class Name:

    def __init__(self, path: str):
        self.basename = os.path.basename(path)  # имя файла с расширением
        self.filename, self.extension = os.path.splitext(self.basename)   # отдельно имя и расширение файла

    def __repr__(self):
        return '<{}>'.format(self.basename)


class Path:

    def __init__(self, path: str):
        self.path = Base(path)  # абсолютный и относительный пути
        self.name = Name(self.path.absolute)  # имя полное (без пути), отдельно имя, отдельно расширение
        self.is_exists = os.path.exists(self.path.absolute)  # признак существования абсолютного пути

    def __repr__(self):
        return '<{}>'.format(self.path.absolute)

    @property
    def parent(self):
        """
        Иерархия родительских директорий до корня файловой системы
        """
        parent = os.path.dirname(self.path.absolute)
        if self.path.absolute == parent:
            return None
        else:
            return Path(parent)

    @property
    def sections(self):
        """
        Составные части пути
        """
        sep = os.path.sep
        return [i for i in self.path.absolute.split(sep) if i]
