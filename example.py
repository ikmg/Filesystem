from cfs import Directory, File


dir = Directory('cfs')
file = File('example.py')

print(dir.path.absolute)
print(dir.path.parts)
print(dir.path.parent().absolute)
print(dir.name.basename)
print(dir.size.proper)
