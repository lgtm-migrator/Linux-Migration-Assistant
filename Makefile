build:
	sudo apt install gir1.2-snapd-1

build_dev:
	make build
	python3 -m venv	.venv && source .venv/bin/activate
	pip install vext vext.gi

test:
	cd src && python3 -m unittest discover tests -v
