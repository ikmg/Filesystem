# Comfort File System
Обертка над встроенными в python модулями: **os, shutil, hashlib, platform, subprocess**

Универсально для разных операционных систем. Возможно совместное использование одной файловой системы одновременно из-под Windows и Linux. 


## **Класс Base**
Базовое представление пути в операционной системе `Base(path: str)`

Атрибуты:
* **.absolute** - абсолютный путь
* **.relative** - относительный путь


## **Класс Name**
Имя объекта в операционной системе `Name(path: str)`

Атрибуты:
* **.basename** - полное имя объекта без указания пути
* **.filename** - имя объекта без расширения
* **.extension** - расширение имени объекта в формате <.*>


## **Класс Path**
Путь к объекту операционной системы `Path(path: str)`

Атрибуты:
*  **.path** - объект класса Base
*  **.name** - объект класса Name
*  **.is_exists** - признак существования абсолютного пути
*  **.parent** - объект класса Path (иерархия родительских директорий до корня файловой системы) 
*  **.sections** - список составных частей абсолютного пути

## **Класс Size**
Размер объекта операционной системы `Size(path: str)`

Атрибуты:
*  **.b** - размер в байтах
*  **.kb** - размер в килобайтах
*  **.mb** - размер в мегабайтах
*  **.gb** - размер в гигабайтах


## **Класс Object**
Объект операционной системы (наследуется от класса Path) `Object(path: str)`

Дополнительные атрибуты:
* **.is_parents_exists** - признак существования всех родительских директорий до корня операционной системы

Методы:
* **size()** - возвращает объект класса Size
* **open()** - открытие объекта в операционной системе
* **copy()** - абстрактный метод копирования объекта, возвращает объект своего класса
* **remove()** - абстрактный метод удаления объекта
* **move()** - перемещение объекта (copy + remove), возвращает объект из метода copy()


## **Класс Dir**
Директория операционной системы (наследуется от класса Object) `Dir(path: str)`

Дополнительные методы:
* **create()** - создает себя если не присутствует в операционной системе
* **join()** - присоединяет к абсолютному пути дочерний элемент, возвращает абсолютный путь
* **children()** - список абсолютных путей объектов, находящихся в директории
* **child_dirs()** - список объектов класса Dir, вложенных в директорию
* **child_files()** - список объектов класса File, вложенных в директорию
* **copy()** - не реализовано
* **remove()** - не реализовано

```
from cfs import Dir

dir = Dir('/home/one/two/three')

print(dir)
>>> </home/one/two/three>

print(dir.path.absolute)
>>> /home/one/two/three

print(dir.path.relative)
>>> ../../../one/two/three

print(dir.is_exists)
>>> False

print(dir.is_parents_exists)
>>> False

print(dir.parent)
>>> </home/one/two>

print(dir.sections)
>>> ['home', 'one', 'two', 'three']
```

## **Класс File**
Файл операционной системы (наследуется от класса Object) `File(path: str)`

Дополнительные методы:
* **md5()** - хэш-сумма файла

```
from cfs import File

file = File('/home/kmg/PycharmProjects/Defenders/storage/defenders.db')

print(file)
>>> </home/kmg/PycharmProjects/Defenders/storage/defenders.db>

print(file.path.absolute)
>>> /home/kmg/PycharmProjects/Defenders/storage/defenders.db

print(file.path.relative)
>>> ../Defenders/storage/defenders.db

print(file.is_exists)
>>> True

print(file.is_parents_exists)
>>> True

print(file.parent)
>>> </home/kmg/PycharmProjects/Defenders/storage>

print(file.sections)
>>> ['home', 'kmg', 'PycharmProjects', 'Defenders', 'storage', 'defenders.db']
```
