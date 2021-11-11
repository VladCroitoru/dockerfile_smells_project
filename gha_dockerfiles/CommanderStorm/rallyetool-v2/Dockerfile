FROM python:3.7-slim

# Install packages needed to run your application (not build deps):
#   mime-support -- for mime types when serving staticfiles files
# We need to recreate the /usr/share/man/man{1..8} directories first because
# they were clobbered by a parent image.
RUN set -ex \
    && RUN_DEPS="mime-support python3-pip" \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt/lists/*

ADD requirements_staging.txt /requirements_staging.txt
RUN pip install --no-cache-dir -r /requirements_staging.txt

ADD requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir /code/
WORKDIR /code/
ADD . /code/

ENV DJANGO_SETTINGS_MODULE=rallyetool.settings

ENV DJANGO_SECRET_KEY=not-needed-in-docker
RUN  python manage.py collectstatic --noinput --settings staging.staging_settings --force-color \
    && rm -f *.sqlite3 \
    && python manage.py makemigrations --noinput \
    && python manage.py migrate --noinput|grep -v "... OK" \
    && echo "import common.fixture as fixture;fixture.showroom_fixture_state_no_confirmation()"|python manage.py shell
ENV DJANGO_SECRET_KEY=

ENV DJANGO_SETTINGS_MODULE=staging.staging_settings

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "staging.staging_wsgi:application"]
