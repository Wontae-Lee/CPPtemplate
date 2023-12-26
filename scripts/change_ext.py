import os


def change_extension(directory, current_extension, new_extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(current_extension):
                current_path = os.path.join(root, file)
                # 새로운 파일명을 생성하여 현재 파일을 새로운 확장자로 변경
                new_path = os.path.splitext(current_path)[0] + new_extension
                try:
                    os.rename(current_path, new_path)
                    print(f"File '{file}' successfully renamed to '{os.path.basename(new_path)}'")
                except OSError as e:
                    print(f"Error renaming file '{file}': {e}")
                    # Handle the exception as needed


def main():
    directory_path = "../include/dumux"
    current_extension = ".cc"  # 현재 확장자
    new_extension = ".cpp"  # 새로운 확장자
    change_extension(directory_path, current_extension, new_extension)


if __name__ == "__main__":
    main()
