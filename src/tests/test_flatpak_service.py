import gi

from packages.services.flatpak_service import FlatpakService

gi.require_version('Flatpak', '1.0')
from gi.repository import Flatpak

class TestFlatpakService:
    FP_CLIENT = FlatpakService()

    def test_list_running_sandboxes(self):
        pass