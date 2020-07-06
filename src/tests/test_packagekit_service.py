from unittest import TestCase
import pytest

from tests.common.utils import has_packagekit_support
from packages.services.packagekit_service import PackageKitService


class TestPackagekitService(TestCase):
    @pytest.mark.skipif(not has_packagekit_support(), reason="Fedora and Ubuntu are the only distro supported")
    def test_list_packages(self):
        def callback_progress(_, __, ___):
            pass

        result = PackageKitService().list_installed_packages(
            progress_callback=callback_progress, progress_user_data=()
        )
        for package in result:
            self.assertTrue("installed" in package.get_data())
