import os
import time

#Files and directories that need copy collect in list
source = ['"D:\\SAVEIT\Downloads\img"']


#Note that names that have spaces need use double quatation inside string

#Reserve copy must be keep in basic reserve directory
target_dir = 'D:\\tmp'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#Use zip command for move files inside zip-archive
zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

#Run to create reserve copy
if os.system(zip_command) == 0:
	print('Reserve copy was created in', target)
else:
	print('Resere copy was failed')