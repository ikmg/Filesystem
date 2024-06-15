import os


def base_name(path: str) -> str:
    """
    Базовое имя объекта операционной системы
    без указания пути к нему
    """
    return os.path.basename(path)


class Name:
    """
    Имя объекта в операционной системе
    """

    def __init__(self, path: str):
        self.basename = os.path.basename(path)  # имя объекта

    def __repr__(self):
        return '<{}>'.format(self.basename)


class DirName(Name):
    """
    Имя директории в операционной системе
    """


class FileName(Name):
    """
    Имя файла в операционной системе
    """

    def __init__(self, path: str):
        super().__init__(path)
        self.name, self.type = os.path.splitext(self.basename)  # отдельно имя и расширение файла
