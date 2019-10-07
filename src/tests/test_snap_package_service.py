from src.packages.services.snap_service import SnapService
import gi

gi.require_version("Snapd", "1")
from gi.repository import Snapd


class TestSnapPackageService:
    SNAP_CLIENT = SnapService()

    def test_list_snaps(self):
        installed_packages = self.SNAP_CLIENT.list_installed_packages()
        assert isinstance(installed_packages, list)
        for package in installed_packages:
            # print(dir(package))
            print(package.get_name())
            assert package.get_install_date() is not None
            assert isinstance(package, Snapd.Snap)
