class PackageFormatter:
    """
        This class is really just a namespace for the function below
    """

    @staticmethod
    def format_package_informations(
        id_package: str,
        name: str,
        platform: str,
        source: str,
        package_type: str,
        dependencies: str,
        version: str,
        is_installed: bool,
        distro="ubuntu",
    ) -> dict:
        """format_package_informations"""
        return {
            "id": id_package,
            "name": name,
            "platform": platform,
            "source": source,
            "package_type": package_type,
            "dependencies": dependencies,
            "version": version,
            "is_installed": is_installed,
            "distro": distro,
        }
