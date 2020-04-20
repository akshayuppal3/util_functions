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
        print(f"Unable to delete reason: {e}")=
        
        
def get_model_json(model_meta_path: Path) -> dict:
    with model_meta_path.open() as json_file:
        model_json = json.load(json_file)
    return model_json


def zip_files(name_list: List[str], file_list: List[pd.DataFrame]) -> bytes:
    outfile = io.BytesIO()
    with zipfile.ZipFile(outfile, 'w') as zf:
        for name, data in zip(name_list, file_list):
            if name.endswith('.csv'):
                zf.writestr(name, data.to_csv())
            else:
                zf.writestr(name, data)
    return outfile.getvalue()

def unzip(path_to_zip_file: Path, destination_dir: Path):
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination_dir)
