import os
from pathlib import Path
import logging
logging.basicConfig(
        format="{levelname} - {asctime} - {message}",
        style='{',
        datefmt='%H:%M:%S',
        level=logging.INFO)
def categorize_files_by_type(folder_path, min_size=None, min_mod=None ):
    if not folder_path.exists():
        print(f'Path {folder_path} does not exist')
        return
    if not folder_path.is_dir():
        print(f'Path {folder_path} is not directory')
        return

    result = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            ext = Path(file).suffix
            path = Path(root) / file
            size = path.stat().st_size
            # Last Modified Date
            lmd = path.stat().st_mtime

            if min_size and size < min_size:
                logging.debug(f'Skipping {path} due to size filter')
                continue
            if min_mod and lmd < min_mod:
                logging.debug(f'Skipping {path} due to last modified filter')
                continue

            if ext in result:
                result[ext].append(path.as_posix())
            else:
                result[ext] = [path.as_posix()]
            logging.info(f'Categorized {path} under {ext}')
    return result

folder_path = Path(r'path_to_folder')




if __name__ == '__main__':
    result =categorize_files_by_type(folder_path)
    print(result)