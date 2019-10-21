from src.packages.services.snap_service import SnapService
import logging
import gi

gi.require_version("Snapd", "1")
from gi.repository import Snapd

logging.basicConfig(filename='app.log', filemode='w', format='%(process)d - %(asctime)s - %(levelname)s - %(message)s')
snap_list_toplaywith = ["spotify", "krop"]


class TestSnapPackageService:
    SNAP_CLIENT = SnapService()

    def test_list_snaps(self):
        installed_packages = self.SNAP_CLIENT.list_installed_packages()
        assert isinstance(installed_packages, list)
        for package in installed_packages:
            assert package.get_install_date() is not None
            assert isinstance(package, Snapd.Snap)

    def test_install_package(self):
        for idx, snap in enumerate(snap_list_toplaywith):
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
                    logging.info("snap installations and tests went ok")
                else:
                    logging.error("Other type of exception: %s...needs to be checked", e)

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
                logging.info("snap deletion and tests went ok")
            else:
                logging.error("Test failed package is not installed before the test starts ")
                raise Exception("Test failed because the required packages are not present in this machine")
