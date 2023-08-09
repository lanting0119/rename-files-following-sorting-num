import os

def get_sorting_order(folder_path):
    file_list = os.listdir(folder_path)  # Get the list of files in the folder
    
    max_num = 0
    for file_name in file_list:
        if file_name[0] not in [str(i) for i in list(range(0,10))]:
            continue
        if max_num <= int(file_name[0:3]):
            max_num = int(file_name[0:3])
    return max_num + 1

def rename_files(folder_path, rule):
    file_list = os.listdir(folder_path)  # Get the list of files in the folder
    max_num = get_sorting_order(folder_path)
    for file_name in file_list:
        if file_name[0] not in [str(i) for i in list(range(0,10))]:
            continue
            
        old_file_path = os.path.join(folder_path, file_name)  # Get the full path of the file
        
        if os.path.isfile(old_file_path):  # Check if it's a file (not a subdirectory)
            
            new_file_name = rule(file_name,max_num,folder_path)  # Apply the renaming rule to get the new file name
            new_file_path = os.path.join(folder_path, new_file_name)  # Get the full path of the new file
            
            os.rename(old_file_path, new_file_path)  # Rename the file

            

# Example renaming rule: add a prefix "new_" to the file name
def add_prefix(file_name,max_num,folder_path): 
    num = file_name[0:3]
    sorting_order = max_num - int(num) 
    sorting_order = str(0)*(3-len(str(sorting_order))) + str(sorting_order) # 转换后保留3位自动填充0
    return sorting_order + file_name[3:]


#### 要修改sorting num!!!
#### 文件重命名，前三位必须是数字
folder_path = r'/Volumes/岚霆 2TB/Downie下载/mac自动化'  # Replace with the actual folder path


rename_files(folder_path, add_prefix)
print('---finished!---')

# folder_path = r'/Volumes/岚霆 2TB/Multivariable calculus'
# file_list = os.listdir(folder_path) 
# print(file_list)

