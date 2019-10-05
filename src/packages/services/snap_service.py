from typing import Dict, List

import gi

gi.require_version("Snapd", "1")
from gi.repository import Snapd


class SnapService:

    def __init__(self):
        self.snap = Snapd.Client().new()

    def list_installed_packages(self) -> List:
        """
          list the packages installed on this machine
        """
        return self.snap.get_snaps_sync(flags=0, names=None)

