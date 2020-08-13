#!/usr/bin/python3
from argparse import ArgumentParser
from pathlib import Path


SOFTWARE_NAME = 'Linux Migration Assistant - CLI'
SOFTWARE_DESCRIPTION = """
This tool is there to help you make the migration of your Linux Machine to your
new Linux machine. We want to help provide the same functionality that macOS has.
"""


if __name__ == '__main__':
    parser = ArgumentParser(prog=SOFTWARE_NAME, description=SOFTWARE_DESCRIPTION)
    backup_restore_group = parser.add_mutually_exclusive_group(required=True)

    backup_restore_group.add_argument('--backup', type=Path, description='The path you want to backup')
    backup_restore_group.add_argument('--restore', type=Path, description='The path you want to restore')

    args = parser.parse_args()

    if args.backup:
        pass

    if args.restore:
        pass
