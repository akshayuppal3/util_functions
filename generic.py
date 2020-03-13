from pathlib import Path
import shutil


def clear_dir_contents(dir: Path):
    """delete the contents of dir iteratively, doesn't delete the sub zips"""
    try:
        for file in dir.iterdir():
            filename = dir.joinpath(file)
            if filename.is_file() or filename.is_symlink():
                filename.unlink()
            else:
                shutil.rmtree(filename)
    except Exception as e:
        print(f"Unable to delete reason: {e}")
