from typing import Callable, Generator

import gi

gi.require_version("PackageKitGlib", "1.0")
from gi.repository import PackageKitGlib


class PackageKitService:
    """
        Regroup common command you would like to use
        with PackageKit
    """

    def __init__(self, progress_publisher=None):
        self.packagekit_client = PackageKitGlib.Client().new()
        self.progress_publisher = progress_publisher

    def list_installed_packages(
        self, progress_callback: Callable, progress_user_data: object
    ) -> Generator:
        """
            List the package that are installed on your
            device
        """
        return (
            p
            for p in self.packagekit_client.get_packages(
                filters=PackageKitGlib.FilterEnum.from_string("INSTALLED"),
                cancellable=None,
                progress_callback=progress_callback,
                progress_user_data=progress_user_data,
            ).get_package_array()
            if "installed" in p.get_data()
        )

    def install_package(self, name: str) -> None:
        # TODO Requires package_name;version;arch;distro as a string to install
        try:
            self.packagekit_client.install_package()
        except Exception as ex:
            print(ex)
