from cfs import Dir, File


file = File('/home/kmg/PycharmProjects/Defenders/storage/defenders.db')
print(file)
print(file.path.absolute)
print(file.path.relative)
print(file.is_exists)
print(file.is_parents_exists)
print(file.parent)
print(file.sections)

print()

dir = Dir('/home/one/two/three')
print(dir)
print(dir.path.absolute)
print(dir.path.relative)
print(dir.is_exists)
print(dir.is_parents_exists)
print(dir.parent)
print(dir.sections)
print(dir.child_dirs())
print(dir.child_files())
