import os


def delete_files_with_extension(directory, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"File '{file}' successfully deleted.")
                except OSError as e:
                    print(f"Error deleting file '{file}': {e}")
                    # Handle the exception as needed


def main():
    directory_path = "../include/dumux/"
    target_extension = ".txt"
    delete_files_with_extension(directory_path, target_extension)


if __name__ == "__main__":
    main()
