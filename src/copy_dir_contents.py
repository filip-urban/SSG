import os
import shutil


def clean_directory(directory_path):
    for file in os.listdir(directory_path):
        if os.path.isfile(directory_path + file):
            os.remove(directory_path + file)
        else:
            shutil.rmtree(directory_path + file)


def copy_files(source, destination):
    clean_directory(destination)
    files = get_list_of_source_paths(source)
    for file in files:
        destination_file_path = file.replace(source, destination, 1)
        if file[-1] == "/":
            print(f"new dirctory: {destination_file_path}")
            os.mkdir(destination_file_path)
        else:
            print(f"source file: {file}")
            print(f"destination file: {destination_file_path}")
            shutil.copy(file, destination_file_path)


def get_list_of_source_paths(source):
    files_result = []
    files = os.listdir(source)
    for file in files:
        file_path = source + file
        if not os.path.isfile(file_path):
            files_result.extend([file_path + "/"])
            files_result.extend(get_list_of_source_paths(file_path + "/"))
        else:
            files_result.append(file_path)
    return files_result
