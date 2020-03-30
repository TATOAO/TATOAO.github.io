import os
from subprocess import call, check_call

# get the number that 
basename = 'base'
file_name_lists = [name.replace('.png','') for name in os.listdir('post_asset') if basename in name]

file_numbs_exist = [int(i.split('_')[-1]) for i in file_name_lists]
file_index = str(max(file_numbs_exist+[0]) + 1)
file_name = basename + '_' + file_index + '.png'

# should be modified if change the directory name
target_path = os.path.join("post_asset",file_name)

# exec the interactive screen capture
call(["screencapture", "-i", target_path])

# snip.rv = '![alt image path: '+ file_name +' failed](' + target_path +' "' +file_name+'")'
print('<img src="{0}" alt="{1}" width="400"/>'.format(target_path, file_name + ' failed'))

call('exit 1', shell=True)
