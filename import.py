import os
if(not os.path.exists("import libs")):
 os.mkdir("import libs")

for i in range(1 ,2):
    os.mkdir(f"import libs/numpy{i}")
