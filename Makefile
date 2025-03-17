test:
	venv/bin/python -m pytest playwright-tests/tests --headed --capture=no

up:
	sudo docker compose up

build:
	sudo docker compose up --build 
