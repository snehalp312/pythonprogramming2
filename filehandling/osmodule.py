import os
file_path ="C:\\Users\\pp\\Desktop\\ITPRENEURallnotespdf\\test90.txt"

if os.path.exists(file_path):
    print("file already exists")
else:
    #create a file
    with open(file_path,'w') as fp:
        fp.write("this is new file")