# Linux-Migration-Assistant - First stages
![Python application](https://github.com/open-tuxnologies/Linux-Migration-Assistant/workflows/Python%20application/badge.svg?branch=develop) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/open-tuxnologies/Linux-Migration-Assistant.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/open-tuxnologies/Linux-Migration-Assistant/context:python)


We aim to bring some of the good stuff we've seen out there to facilitate migration from a computer to another! Or from a Distribution to an another!

# Planned Features

1. Backup your laptop on a USB Key or your HDD
2. Restore from a HDD or USB key 
3. Restore your laptop from another laptop that is already running linux ( Thunderbolt/USB-C/USB )
4. Blockchain Machine Deployment 1-to-N & 1-to-1 ( Later )

## Requirements

* Python 3.7+
* pydbus
* PackageKit

## Quick start

```bash
  ## On Ubuntu
  make setup_dev
  source .venv/bin/activate
```

## Supported Distribution

* Ubuntu 18.04 +

We even plan to allow restore from Windows 10 to Linux!

For now we aim only the desktop and laptops but we might venture into the server world or maybe the cloud ... Why not!
