from typing import Callable

from packages.formatter.package_formatter import PackageFormatter

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
    ):
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

    def remove_package(self, name: str):
        pass

    def get_installed_packages(
        self, callback_ready: Callable, callback_progress=None
    ) -> None:
        self.packagekit_client.get_packages_async(
            filter=PackageKitGlib.FilterEnum.NONE,
            cancellable=None,
            callback_progress=callback_progress,
            progress_user_data=None,
            callback_ready=callback_ready,
            ready_user_data=None,
        )

    def _create_dict_from_array(self, package_array):
        """_create_dict_from_array

        extract data from each Package found

        :param package_array: [ PackageKitGlib.Package, ...]
        :returns : list of dictionnaries with all the informations in the Package
        """
        packages = []
        for package in package_array:
            packages.append(self._extract_package_to_dict(package=package))
        return packages

    def _extract_package_to_dict(self, package):
        """_extract_package_to_dict

        Use the formatter to return a dictionnary
        filled all the informations found in the Package object

        :param package: PackageKitGlib.Package
        :returns dict: Dictionnary of the information in the Package
        """
        return PackageFormatter.format_package_informations(
            id_package=package.get_id(),
            name=package.get_name(),
            platform=package.get_arch(),
            source=package.get_data(),
            package_type="apt",  # TODO Should in a variable ( find package manager )
            version=package.get_version(),
            is_installed=package.get_data(),
        )

    def _extract_information_from_strings(self, package):
        """__extract_information_from_strings

            Some Package informations are stored in
            strings or Enums. This function
            has for purpose to extract those embedded informations

        :doc: https://lazka.github.io/pgi-docs/#PackageKitGlib-1.0/classes/Package.html#PackageKitGlib.Package
        :param package:
        :return TBD -> TODO find out what can be extracted
        """
        # TODO Extract data from the Package Data
        pass
