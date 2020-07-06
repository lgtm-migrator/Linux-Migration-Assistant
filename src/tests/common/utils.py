from distro import linux_distribution


UBUNTU_NAME_STRING = "Ubuntu"
FEDORA_NAME_STRING = "Fedora"


def has_packagekit_support() -> bool:
    distro = linux_distribution()[0]
    return distro is UBUNTU_NAME_STRING or distro is FEDORA_NAME_STRING
