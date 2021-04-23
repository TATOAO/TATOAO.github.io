import os
from datetime import datetime

cwd = os.listdir(".")
cwd = [i for i in cwd if '.md' in i]
print(cwd)

for file in cwd:
    t = os.path.getmtime(file)
    date = datetime.fromtimestamp(t).strftime('%Y-%m-%d')

    if file[0:10] == date:
        print(file + ' no need modified')
        continue
    else:
        print(file)
        os.rename(file,date+file[10:])
