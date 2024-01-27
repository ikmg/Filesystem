from fs import File

file = File('fs.py')

print('File absolute path:', file.path)
print('Directory absolute path:', file.dir.path)

print('File path from work directory:', file.rel_path)
print('Directory path from work directory:', file.dir.rel_path)

print('Is file exists:', file.is_exists)
print('Is directory exists:', file.dir.is_exists)

print('Base filename:', file.base_name)
print('Filename extension:', file.extension)
