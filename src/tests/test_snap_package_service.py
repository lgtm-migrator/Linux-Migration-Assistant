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
        for idx,snap in enumerate(snap_list_toplaywith):
            check_snap = SnapService.list_one_package(snap)
            if check_snap is None:
                flags = Snapd.InstallFlags.NONE  # CLASSIC, DEVMODE, DANGEROUS, JAILMODE
                check_snap = snap_list_toplaywith[idx]
                channel = None  # default channel
                revision = None  # default revision
                progress_callback = None
                new_installed_snap = self.SNAP_CLIENT.install_package_name(flags, check_snap, channel, revision, progress_callback, None, None)
                assert new_installed_snap is True
                print("snap installations and tests went ok, now we delete the tested snaps")
        # for snap in snap_list_toplaywith:
        #     self.SNAP_CLIENT.delete_package(snap)
