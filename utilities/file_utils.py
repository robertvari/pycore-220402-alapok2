import os


def get_files(root_folder, file_list):
    folder_content = [os.path.join(root_folder, i) for i in os.listdir(root_folder)]

    # get all files in folder_content and add them to file_list
    for i in folder_content:
        if os.path.isfile(i):
            file_list.append(i)

    subfolders = []
    for i in folder_content:
        if os.path.isdir(i):
            subfolders.append(i)

    for folder in subfolders:
        get_files(folder, file_list)


my_files = []
get_files(
    r"C:\Work\_PythonSuli\pycore-220402\recursion_example_folder",
    my_files
)
print(my_files)