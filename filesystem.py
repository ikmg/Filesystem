import os
import shutil
import hashlib
import platform
import subprocess


def _get_linux_path_(path: str) -> str:
    """
    Преобразователь пути к объектам в формат Linux
    """
    if isinstance(path, str):
        return path.replace('\\', '/')
    else:
        raise ValueError('path <{}> must be string'.format(path))


def _get_windows_path_(path: str) -> str:
    """
    Преобразователь пути к объектам в формат Windows
    """
    if isinstance(path, str):
        return path.replace('/', '\\')
    else:
        raise ValueError('path <{}> must be string'.format(path))


def _convert_path_(path: str) -> str:
    """
    Преобразователь пути к объектам в зависимости от операционной системы
    """
    if platform.system() == 'Windows':
        # Windows
        return _get_windows_path_(path)
    else:
        # Linux, MacOS
        return _get_linux_path_(path)


def _start_(path) -> None:
    """
    Открытие пути в операционной системе
    """
    if platform.system() == 'Darwin':
        # MacOS
        subprocess.call(('open', path))
    elif platform.system() == 'Windows':
        # Windows
        subprocess.call(('start', "", path), shell=True)
    else:
        # Linux
        subprocess.run(['xdg-open', path])


class _Path_:
    """
    Путь к объектам операционной системы
    """

    def __init__(self, path: str):
        """
        Вычисление абсолютного пути при инициализации
        """
        self.path = os.path.abspath(_convert_path_(path))

    def __repr__(self):
        return self.path

    @property
    def parent_dir(self):
        # TODO реализовать -> None | Dir в имени метода
        """
        Путь к родительской директории
        """
        parent = os.path.dirname(self.path)
        return None if parent == self.path else Dir(parent)

    def start(self) -> None:
        """
        Открытие в операционной системе
        """
        _start_(self.path)

    @property
    def is_exists(self) -> bool:
        """
        Проверка существования пути к объекту
        """
        return os.path.exists(self.path)

    @property
    def rel_path(self) -> str:
        """
        Относительный путь (без пути к директории вызова (рабочей директории))
        """
        return os.path.relpath(self.path, self.work_dir.path)

    @property
    def work_dir(self):
        # TODO реализовать -> Dir в имени метода
        """
        Директория вызова программы (рабочая директория)
        """
        return Dir(os.path.abspath(os.curdir))


class File(_Path_):
    """
    Файл операционной системы
    """
    def __init__(self, path: str):
        super().__init__(path)
        if not os.path.isfile(self.path):
            raise ValueError('path <{}> is not a file'.format(self.path))

    def copy(self, destination: str):
        # TODO как написать -> экземпляр этого же класса
        """
        Копирование файла
        """
        shutil.copyfile(self.path, destination)
        return File(destination)

    def delete(self) -> None:
        """
        Удаление файла
        """
        os.remove(self.path)

    def md5(self) -> str:
        """
        Хэш-сумма файла
        """
        with open(self.path, 'rb') as f:
            m = hashlib.md5()
            while True:
                data = f.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()

    @property
    def filename(self) -> str:
        """
        Имя файла с расширением
        """
        return os.path.basename(self.path)

    @property
    def name(self) -> str:
        """
        Имя файла файла
        """
        filename, extension = os.path.splitext(self.filename)
        return filename

    @property
    def extension(self) -> str:
        """
        Расширение файла
        """
        filename, extension = os.path.splitext(self.filename)
        return extension


class Dir(_Path_):
    """
    Директория операционной системы
    """
    def __init__(self, path: str):
        super().__init__(path)
        if not os.path.isdir(self.path):
            raise ValueError('path <{}> is not a directory'.format(self.path))

    def create(self) -> None:
        """
        Создание директории (самой себя) если она не присутствует в операционной системе
        """
        if not self.is_exists:
            os.mkdir(self.path)

    def add_dir(self, dir_name: str):
        # TODO как написать -> экземпляр этого же класса
        """
        Добавление дочерней директории к пути директории
        """
        return Dir(os.path.join(self.path, dir_name))

    def add_file(self, file_name: str) -> File:
        """
        Добавление файла к пути директории
        """
        return File(os.path.join(self.path, str(file_name)))

    def files(self):
        # TODO реализовать -> dict[str: list[Dir | File | str]] в имени метода
        """
        Словарь со списками файлов и директорий в директории
        """
        result = {
            'dirs': [],
            'files': [],
            'other': []
        }
        content = os.listdir(self.path)
        for item in content:
            try:
                result['dirs'].append(self.add_dir(item))
            except:
                try:
                    result['files'].append(self.add_file(item))
                except:
                    result['other'].append(item)
        return result
