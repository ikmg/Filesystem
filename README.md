# Comfort File System
Модуль для работы с файловой системой для десктопных приложений.

Обертка над встроенными в python модулями: `os`, `shutil`, `hashlib`, `platform`, `subprocess`.

Универсально для разных операционных систем.


## **Встроенный класс Path**
Путь к объекту операционной системы `Path(path: str)`.

При инициализации выдает исключение в случаях, когда `path` не является объектом `str`. 
При работе с файловой системой одновременно из-под Windows и Linux конвертирует входной параметр в формат операционной системы.

Атрибуты:
* `.absolute: str` - абсолютный путь к объекту операционной системы;
* `.relative: str` - относительный путь к объекту операционной системы.

Свойства:
* `.is_exists: bool` - признак существования объекта в операционной системе.

Методы:
* `.parts(): list` - список элементов в `self.absolute`, разделенных на составные части по системному сепаратору;
* `.parent() -> Path` - возвращает родительскую директорию как объект класса `Path`.


## **Встроенный класс Name**
Имя объекта операционной системы `Name(path: str)`.

Атрибуты:
* `.basename: str` - полное имя объекта операционной системы (используется в классах `Directory` и `File`);
* `.name: str` - имя файла операционной системы (используется в классе `File`);
* `.type: str` - расширение файла операционной системы (используется в классе `File`).


## **Встроенный класс Size**
Размер объекта операционной системы `Size(size: int)`.

Атрибуты:
* `.b: int` - размер байтах;
* `.kb: float` - размер килобайтах;
* `.mb: float` - размер мегабайтах.
* `.gb: float` - размер гигабайтах.

Свойства:
* `.proper: str` - размер в удобном для человека представлении.


## **Абстрактный класс ObjectOS**
Объект операционной системы `ObjectOS(path: str)`.

Атрибуты:
* `.path: Path` - путь к объекту операционной системы, экземпляр класса `Path`;
* `.name: Name` - имя объекта операционной системы, экземпляр класса `Name`;
* `.size: Size` - размер объекта операционной системы, экземпляр класса `Size`.

Методы:
* `.open()` - открывает `self.path.absolute` объект в операционной системе;
* `.copy(destination: str) -> ObjectOS` - копирует `self.path.absolute` объект в операционной системе по указанному в `destination` пути, возвращает новый объект этого же класса;
* `.remove()` - удаляет `self.path.absolute` объект в операционной системе;
* `.move(destination: str) -> ObjectOS` - перемещает `self.path.absolute` объект в операционной системе по указанному в `destination` пути, возвращает новый объект этого же класса;
* `.get_size()` - вычисляет размер `self.path.absolute` объекта в операционной системе, обновляет атрибут `.size`.


## **Класс File**
Файл операционной системы `File(path: str)`, наследуется от класса `ObjectOS`.

При инициализации дополнительно выдает исключение в случаях, когда объект операционной системы указанный в `path` не является файлом. 

Дополнительные методы:
* `.md5() -> str` - хэш-сумма файла.


## **Класс Directory**
Директория операционной системы `Directory(path: str)`, наследуется от класса `ObjectOS`.

При инициализации дополнительно выдает исключение в случаях, когда объект операционной системы указанный в `path` не является директорией. 

Дополнительные методы:
* `.create()` - создает `self.path.absolute` директорию, если она не присутствует в операционной системе;
* `.join(child: str) -> str` - присоединяет к абсолютному пути дочерний элемент `child`, возвращает абсолютный путь;
* `.child_list() -> list` - список абсолютных путей объектов, находящихся в директории;
* `.child_dirs() -> list` - список объектов класса `Directory`, вложенных в директорию;
* `.child_files() -> list` - список объектов класса `File`, вложенных в директорию.
