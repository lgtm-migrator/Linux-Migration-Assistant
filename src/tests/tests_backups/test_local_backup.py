from contextlib import contextmanager
from pathlib import Path

from backups.local_backup import LocalBackup


class TestLocalBackup:
    DEFAULT_LOCAL_PATH = Path.home()
    DEFAULT_BACKUP_PATH = Path.cwd()

    def __init__(self):
        pass

    @contextmanager
    def init_local_backup(self, local_path=None, backup_path=None) -> LocalBackup:
        if local_path is None:
            local_path = self.DEFAULT_LOCAL_PATH
        if backup_path is None:
            backup_path = self.DEFAULT_BACKUP_PATH
        local_backup = LocalBackup(local_path=local_path, backup_path=backup_path)
        try:
            yield local_backup
        finally:
            del local_backup

    def test_get_folder_structure(self):
        with self.init_local_backup() as local_backup:
            folder_structure = local_backup._get_folder_structure()
            assert isinstance(folder_structure, str)
