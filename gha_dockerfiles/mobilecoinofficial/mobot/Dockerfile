# syntax=docker/dockerfile:1.3
FROM python:3.9.5

ENV PYTHONUNBUFFERED=1

RUN  addgroup --system --gid 1000 app \
  && addgroup --system --gid 2000 app-data \
  && adduser --system --ingroup app --uid 1000 app \
  && usermod -a -G 2000 app \
  && mkdir -p /signald \
  && chown app:app /signald

RUN  apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y ca-certificates \
  && apt-get clean \
  && rm -r /var/lib/apt/lists

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY src/ /app/
COPY privacy/ /privacy/
COPY .docker/start_*.sh /usr/local/bin/

# Run static content and database migration generation
RUN  python manage.py collectstatic --noinput \
  && python manage.py makemigrations \
  && python manage.py makemigrations mobot_client

USER app
EXPOSE 8000
VOLUME /signald
CMD [ "/bin/echo 'Start Client: /usr/local/bin/startup_client.sh\nStart Admin /usr/local/bin/startup_admin.sh'" ]
