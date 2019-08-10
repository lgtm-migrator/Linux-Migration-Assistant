from unittest import TestCase

from packages.services.packagekit_service import PackageKitService


class TestPackagekitService(TestCase):

    def test_list_packages(self):
        list_packages = PackageKitService().list_installed_packages()
        print(list_packages)
