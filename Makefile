SHELL := /bin/bash

build:
	sudo apt install gir1.2-snapd-1 libgirepository1.0-dev python3-venv python3-cairo-dev libcairo2-dev python3-dev

setup_dev:
	make build
	python3 -m venv	.venv && source .venv/bin/activate && pip install vext vext.gi && pip install -r requirements/dev.txt

run_unittests:
	cd src && python3 -m pytest -v
