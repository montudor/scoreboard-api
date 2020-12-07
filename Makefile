build:
	docker-compose build

up:
	docker-compose up -d

start:
	docker-compose start

stop:
	docker-compose stop

shell-web:
	docker exec -ti tetris-web bash

shell-db:
	docker exec -ti tetris-db bash

logs-web:
	docker-compose logs web

logs-db:
	docker-compose logs db

collectstatic:
	docker exec tetris-web /bin/sh -c "python manage_production.py collectstatic --noinput"

createsuperuser:
	docker exec -ti tetris-web /bin/sh -c "python manage_production.py createsuperuser"

migrate:
	docker exec -ti tetris-web /bin/sh -c "python manage_production.py migrate"

backup-db:
	docker exec -t tetris-db pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql

