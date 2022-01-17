from pathlib import Path


def folder_exists(folder_name):
    return Path(folder_name).is_dir()


def create_folder(folder):
    try:
        if not folder_exists(folder):
            Path(folder).mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Error: {e.strerror}")


def delete_folder(folder):
    try:
        if folder_exists(folder):
            Path(folder).rmdir()
    except OSError as e:
        print(f"Error: {e.strerror}")


def sync_folder(folder):
    delete_folder(folder)
    create_folder(folder)


def zipFolder():
    return None
