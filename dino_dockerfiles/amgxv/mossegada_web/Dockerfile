FROM python:3.6.5-slim

ENV DB_NAME=postgres \
DB_USER=postgres \
DB_PASS=postgres \
DB_HOST=postgres \
DB_PORT=5432 \
SMTP_HOST=smtp \
SMTP_USER=username \
SMTP_PASS=password \
SMTP_PORT=25 \
SMTP_USE_TLS=False \
DEFAULT_FROM_EMAIL=noreply@localhost.com \
REDIS_HOST=localhost \
REDIS_PORT=6379 \
REDIS_DB=1 \
GMAPS_API=api 

RUN mkdir /mossegada_app
COPY ./mossegada_app /mossegada_app/
WORKDIR /mossegada_app

RUN pip install -r requirements.txt && python manage.py collectstatic --noinput
