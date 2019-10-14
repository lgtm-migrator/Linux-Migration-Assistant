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
         :return: List
        """
        return self.snap.get_snaps_sync(flags=0, names=None)

    def list_one_package(self, name) -> Snapd.Snap:
        """
          Get information of a single installed snap. If the snap does not exist an error occurs
        :return: Snapd.Snap
        """
        return self.snap.get_snap_sync(name, None)

    def install_package_name(self, flags, name, channel, revision, progress_callback, pgd, clble) -> bool:
        """
        Install package with the name
        :param package: name of the snap package
        """
        return self.snap.install2_sync(flags, name, channel, revision, progress_callback, pgd, clble)

    def delete_package(self, name, progress_callback, progress_callback_data, cancellable) -> bool:
        """
         Delete package passed as args
        :param package: package to delete
        """
        return self.snap.remove_sync(name, progress_callback, progress_callback_data, cancellable)