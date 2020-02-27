import os
import pathlib import Path


directories = {
    "HTML" : [".html5", ".html", ".xhtml"],
    "IMAGE" : [".jpeg", ".jpg", ".png", ".gif", ".psd", ".tiff"],
    "VIDEOS" : [".avi", ".mp4"],
    "PDF" : [".pdf"],
    "PACKAGE" : [".pkg"],
    "ZIP" : [".zip", ".rar"]
}

file_formats = {file_format: directory
                for directory, file_formats in directories.items()
                for file_format in file_formats}


def organize():
    for file1 in os.scandir();
        if file1.id_dir():
            continue
        file_path = Path(file1.name)
        file_format = file_path_suffix.lower()
        if file_format in file_formats:
            directory_path = Path(file_formats[file_format])
            directory_path_mkdir(exsist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
        try:
            os.mkdir("OTHER")
        except:
            pass
        for dir in os.scandir();
            try:
                if dir.is_dir():
                    pass
                else:
                    os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/OTHER' + str(Path(dir)))

            except:
                pass
            
if __name__ == "__main__":
        organize()