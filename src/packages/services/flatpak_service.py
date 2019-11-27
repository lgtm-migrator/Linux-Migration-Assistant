from typing import Dict, List

import gi

gi.require_version('Flatpak', '1.0')
from gi.repository import Flatpak
from gi.repository import GLib


class FlatpakService:

    def __init__(self):
        self.flatpak = Flatpak.Installation()

    def list_running_sandboxes(self) -> List:
        """
          list the running flatpak boxes
         :return: List
        """
        return self.flatpak.get_all()

    def get_sandbox_infos(self) -> GLib.Keyfile:
        """
        Gets a keyfile that holds information about the running sandbox.
        This file is available as /.flatpak-info inside the sandbox as well.
        The most important data in the keyfile is available with separate getters,
         but there may be more information in the keyfile.
        :return: GLib.Keyfile
        """

    def get_sandbox_app_id(self) -> str:
        """
        Gets the application ID of the application running in the instance.
        Note that this may return None for sandboxes that don’t have an application.
        :return: str or None
        """
        self.flatpak.get_app()

    def get_sandbox_pid(self) -> int:
        """
         Get the process id
        :return: int
        """
        return self.flatpak.get_pid()

    def is_sandbox_running(self) -> bool:
        """
          Finds out if the sandbox represented by self is still running.
        :return: True or False
        """
        return self.flatpak.is_running()

    def get_ref_runtime(self) -> str:
        """
          Gets the ref of the runtime used in the instance.
        :return: str
        """
        return self.flatpak.get_runtime()

    def get_instance_app_arch(self) -> str:
        """
          Gets the architecture of the application running in the instance.
        :return: str
        """
        return self.flatpak.get_arch()

