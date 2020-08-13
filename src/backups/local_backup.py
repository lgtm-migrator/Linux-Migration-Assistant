from pathlib import Path
from glob import glob


class LocalBackup:
    """
    Takes care of restore and backup from  the machine
    to a external HDD or on the machine itself
    """
    def __init__(self, local_path: Path, backup_path: Path):
        self._local_folder = local_path
        self._backup_folder = backup_path

    def backup_local_folder(self):
        """
        Public function that takes care of making a backup
        """
        pass

    def _get_folder_structure(self):
        return glob(pathname=self._local_folder)
