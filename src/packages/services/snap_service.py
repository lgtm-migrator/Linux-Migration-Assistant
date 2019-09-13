from typing import Dict, List

import gi

gi.require_version("Snapd", "1")
from gi.repository import Snapd

class SnapService:

    def __init__(self):
        self.snap = Snapd.Client().new()


    def list_packages(self) -> List:
        """
          list the packages installed on this machine
        """
        installed_snaps = self.snap_client.get_snaps_sync(flags=0, names=None)
        return installed_snaps


    def install_package(self, package):
        """
        Install each package which is inside the list
        :param package: name of the snap package

        """
        self.snap.install2_sync(name=package)


    def delete_package(self, package):
        """
        Delete package passed as args
        :param package: package to delete
        """
        self.snap_client.remove_sync(name=package)