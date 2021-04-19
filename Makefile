build:
	docker-compose -f docker-compose.prod.yml build
up:
	docker-compose -f docker-compose.prod.yml up
down:
	docker-compose down -v
migrate:
	docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate --noinput
static:
	docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --no-input --clear
