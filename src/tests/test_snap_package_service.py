from packages.services.snap_service import SnapService
import gi

gi.require_version("Snapd", "1")
from gi.repository import Snapd


class TestSnapPackageService:
    SNAP_CLIENT = SnapService()
    snap_list_toplaywith = {"spotify", "krop"}

    def test_list_snaps(self):
        installed_packages = self.SNAP_CLIENT.list_installed_packages()
        assert isinstance(installed_packages, list)
        for package in installed_packages:
            assert package.get_install_date() is not None
            assert isinstance(package, Snapd.Snap)

    def test_install_package(self):
        for snap in self.snap_list_toplaywith:
            flags = Snapd.InstallFlags.NONE  # CLASSIC, DEVMODE, DANGEROUS, JAILMODE
            channel = None  # default channel
            revision = None  # default revision
            progress_callback = None
            new_installed_snap = self.SNAP_CLIENT.install_package_name(flags, snap, channel, revision,
                                                                       progress_callback, None, None)
            assert new_installed_snap is True

    def test_remove_package(self):
        for snap in self.snap_list_toplaywith:
            progress_callback = None
            progress_callback_data = None
            cancellable = None
            removed_snap = self.SNAP_CLIENT.delete_package(snap, progress_callback,
                                                           progress_callback_data,
                                                           cancellable)
            assert removed_snap is True

