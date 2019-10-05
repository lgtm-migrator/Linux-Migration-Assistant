SHELL := /bin/bash

build:
	sudo apt install gir1.2-snapd-1 libgirepository1.0-dev

setup_dev:
	make build
	python3 -m venv	.venv && source .venv/bin/activate && pip install vext vext.gi && pip install -r requirements/dev.txt

test:
	cd src && python3 -m unittest discover tests -v
