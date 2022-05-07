import os.path
dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = ['%s:' %d for d in dl if os.path.exists('%s:' % d)]
print(drives)