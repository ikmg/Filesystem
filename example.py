from cfs import Directory, File


dir = Directory('cfs')
file = File('example.py')

print('Directory:', dir)
print('\tparent:', dir.path.parent())
print('\tparts:', dir.path.parts())

new_path = dir.join('cfs_d')
new_dir = dir.copy(new_path)
print(new_dir)
new_dir.remove()

q = 1
