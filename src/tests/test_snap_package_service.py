from src.packages.services.snap_service import SnapService
import gi

gi.require_version("Snapd", "1")
from gi.repository import Snapd

snap_list_toplaywith = ["spotify", "krop"]


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

    def test_install_package(self):
        for idx, snap in enumerate(snap_list_toplaywith):
            print("snap is " + snap)
            name = str(snap)
            try:
                check_snap = self.SNAP_CLIENT.list_one_package(name)
            except Exception as e:
                if e.domain == 'snapd-error-quark':
                    flags = Snapd.InstallFlags.NONE  # CLASSIC, DEVMODE, DANGEROUS, JAILMODE
                    check_snap = snap_list_toplaywith[idx]
                    channel = None  # default channel
                    revision = None  # default revision
                    progress_callback = None
                    new_installed_snap = self.SNAP_CLIENT.install_package_name(flags, check_snap, channel, revision,
                                                                               progress_callback, None, None)
                    assert new_installed_snap is True
                    print("snap installations and tests went ok")
                else:
                    print("Other type of exception...needs to be checked")
                    return False

    def test_remove_package(self):
        for idx, snap in enumerate(snap_list_toplaywith):
            print("checking if snap package named " + snap + " exists")
            check_snap = self.SNAP_CLIENT.list_one_package(snap)
            if check_snap is not None:
                check_snap = str(snap_list_toplaywith[idx])
                print("check snap " + check_snap)
                progress_callback = None
                progress_callback_data = None
                cancellable = None
                removed_snap = self.SNAP_CLIENT.delete_package(check_snap, progress_callback,
                                                               progress_callback_data,
                                                               cancellable)
                assert removed_snap is True
                print("snap deletion and tests went ok")
            else:
                print("Test failed package is not installed before the test starts ")
                return False
