import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# sort files by ext and copy to target dir
def process_file(file_path, target_dir):
    ext = file_path.suffix[1:]
    ext_dir = target_dir / ext
    ext_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file_path, ext_dir / file_path.name)

# process dir and subdirs
def process_directory(source_dir, target_dir):
    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = Path(root) / file
                executor.submit(process_file, file_path, target_dir)

if __name__ == "__main__":
    import sys
    source_dir = Path(sys.argv[1])
    target_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    process_directory(source_dir, target_dir)
