from time import sleep
from unittest import TestCase

from packages.services.packagekit_service import PackageKitService


class TestPackagekitService(TestCase):
    def test_list_packages(self):
        def callback_progress(_, __, ___):
            pass

        result = PackageKitService().list_installed_packages(
            progress_callback=callback_progress, progress_user_data=()
        )
        for package in result:
            self.assertTrue("installed" in package.get_data())
