-include .env

venv:
	python3 -m venv .venv
	source .venv/bin/activate

list:
	pip list

uninstall_all:
	pip freeze | xargs pip uninstall -y

install_all:
	pip install -r requirements.txt

appinstall:
	pip install $(package)

build:
	 docker-compose build

fresh_build:
	docker-compose build --no-cache

start:
	docker compose up -d

stop:
	docker-compose down

restart:
	docker-compose down
	docker-compose up -d

logs:
	docker-compose logs -f


start_app:
	docker exec -it ai_trading /bin/sh


rand_key:
	openssl rand -base64 $(legnth)

agno_upgrade:
	pip install -U agno --no-cache-dir



