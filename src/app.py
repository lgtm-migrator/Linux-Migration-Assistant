#!/usr/bin/python3
from argparse import ArgumentParser


SOFTWARE_NAME = "Linux Migration Assistant - CLI"
SOFTWARE_DESCRIPTION = """
This tool is there to help you make the migration of your Linux Machine to your
new Linux machine. We want to help provide the same functionality that macOS has.
"""


if __name__ == "__main__":
    args = ArgumentParser(prog=SOFTWARE_NAME, description=SOFTWARE_DESCRIPTION)
