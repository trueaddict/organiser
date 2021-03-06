import os
from pathlib import Path

directories = {
    "html" : [".html5", ".html", ".xhtml"],
    "image" : [".jpeg", ".jpg", ".png", ".gif", ".psd", ".tiff"],
    "videos" : [".avi", ".mp4"],
    "pdf" : [".pdf"],
    "package" : [".pkg"],
    "zip" : [".zip", ".rar"]
}

file_formats = {file_format: directory
                for directory, file_formats in directories.items()
                for file_format in file_formats}


def organize():
    for file1 in os.scandir():
        if file1.is_dir():
            continue
        file_path = Path(file1.name)
        file_format = file_path.suffix.lower()
        if file_format in file_formats:
            directory_path = Path(file_formats[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
        try:
            os.mkdir("other")
        except:
            pass
        for dir in os.scandir():
            try:
                if dir.is_dir():
                    continue
                else:
                    os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/other/' + str(Path(dir)))

            except:
                pass

if __name__ == "__main__":
        organize()