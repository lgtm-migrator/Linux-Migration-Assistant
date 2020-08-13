SHELL := /bin/bash

build:
	sudo apt install -y python3-pip gir1.2-snapd-1 packagekit gir1.2-packagekitglib-1.0 libgirepository1.0-dev python3-venv python3-cairo-dev libcairo2-dev python3-dev

setup_dev:
	make build
	python3 -m venv	.venv && source .venv/bin/activate && pip install vext vext.gi && pip install -r requirements/dev.txt

build_setup_test:
	make build
	pip3 install -r requirements/test.txt

codestyle:
	flake8

run_unittests:
	sudo su -c "python3 -m pip install -r requirements/test.txt && cd src && coverage run -m pytest -v && coverage report"
