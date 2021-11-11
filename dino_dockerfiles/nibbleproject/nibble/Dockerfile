FROM python:3.8.5

ENV DJANGO_SETTINGS_MODULE=nibble.settings.production
ENV DATABASE_NAME=nibble
ENV DATABASE_USER=test
ENV PORT=5000

RUN apt-get update && apt-get -y install postgresql-client && pip install pipenv

COPY ["./Pipfile.lock", "./Pipfile", "/app/"]
WORKDIR /app/

RUN pipenv install --system

COPY . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 5000

ENTRYPOINT ["docker/run.sh"]
CMD ["start"]
