import os

def get_sorting_order(folder_path,char):
    file_list = os.listdir(folder_path)  # Get the list of files in the folder
    
    max_num = 0
    
    for file_name in file_list:
        nPos = file_name.find(char)
        
        if file_name[nPos+1] not in [str(i) for i in list(range(0,10))]:
            continue
        if max_num <= int(file_name[nPos+1:nPos+1+3]):
            max_num = int(file_name[nPos+1:nPos+1+3])
    return max_num + 1

def rename_files(folder_path, rule,char):
    file_list1 = os.listdir(folder_path)  # Get the list of files in the folder
    file_list = []
    for file_name in file_list1:
        if file_name[0] == '.':
            continue
        file_list.append(file_name)
    max_num = get_sorting_order(folder_path,char)

    for file_name in file_list:
        # print(file_name)
        nPos = file_name.find(char)
        # print(nPos)
        # print(file_name[nPos+1])
        if file_name[nPos+1] not in [str(i) for i in list(range(0,10))]:
            print('a')
            continue
            
        old_file_path = os.path.join(folder_path, file_name)  # Get the full path of the file
        
        if os.path.isfile(old_file_path):  # Check if it's a file (not a subdirectory)
            
            new_file_name = rule(file_name,max_num,folder_path,char)  # Apply the renaming rule to get the new file name
            new_file_path = os.path.join(folder_path, new_file_name)  # Get the full path of the new file
            
            os.rename(old_file_path, new_file_path)  # Rename the file            

# Example renaming rule: add a prefix "new_" to the file name
def add_prefix(file_name,max_num,folder_path,char): 
    nPos = file_name.find(char)
    # print(file_name)
    # print(nPos)
    if file_name[nPos+1] in [str(i) for i in list(range(0,10))]:
        num = file_name[nPos+1:nPos+1+3]
    sorting_order = max_num - int(num) 
    sorting_order = str(0)*(3-len(str(sorting_order))) + str(sorting_order) # 转换后保留3位自动填充0
    return sorting_order + file_name[nPos+4:]

#### 要修改sorting num!!!
#### 文件重命名，前三位必须是数字
folder_path = r'/Volumes/岚霆 2TB/Downie下载/CCC_youtube/NicheNet_CCC_youtube'  # Replace with the actual folder path
char = '-' #设定分隔符

rename_files(folder_path, add_prefix,char)
print('---finished!---')
# folder_path = r'/Volumes/岚霆 2TB/Multivariable calculus'
# file_list = os.listdir(folder_path) 
# print(file_list)

