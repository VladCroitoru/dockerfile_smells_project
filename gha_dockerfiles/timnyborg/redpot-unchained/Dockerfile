# Adapted from https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/
# Specify debian version to avoid breaking on new version releases (needs syncing with microsoft packages)
FROM python:3.7-slim-buster

# Create a group and user to run our app
ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

# Add microsoft package repository
RUN apt-get update && apt-get install -y curl gnupg \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Install packages needed to run your application (not build deps):
ENV ACCEPT_EULA=Y
RUN apt-get update && apt-get install -y --no-install-recommends \
      # uwsgi static serving
      libpcre3 \
      mime-support \
      # odbc drivers
      msodbcsql17 \
      # weasyprint prereqs  # cairo is not needed once we move to bullseye and weasyprint >=54
      libcairo2 \
      libpango-1.0-0 \
      libpangoft2-1.0-0 \
      libpangocairo-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Python packages
COPY requirements.txt /requirements.txt
COPY dependencies.txt /dependencies.txt

# Install build deps, install python packages, then remove build deps in a single step - key for keeping size down
RUN BUILD_DEPS=" \
    build-essential \
    libpcre3-dev \
    libpq-dev \
    $(cat /dependencies.txt) \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && pip install --no-cache-dir -r /requirements.txt \
    && pip install --no-cache-dir uwsgi \
    \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*

# Application code
RUN mkdir /code/ \
    && chown ${APP_USER}:${APP_USER} /code/
WORKDIR /code/
ADD --chown=${APP_USER}:${APP_USER} . /code/

# uWSGI will listen on this port
EXPOSE 8000

# Call collectstatic
RUN python manage.py collectstatic --noinput \
# build the mkdocs
  && mkdocs build

# Tell uWSGI where to find your wsgi file
ENV UWSGI_WSGI_FILE=redpot/wsgi.py

# Base uWSGI configuration
ENV UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# Number of uWSGI workers and threads per worker
ENV UWSGI_WORKERS=2 UWSGI_THREADS=4

# uWSGI static file serving configuration
ENV UWSGI_STATIC_MAP="/static/=/code/static/" UWSGI_STATIC_INDEX="index.html"
ENV UWSGI_STATIC_EXPIRES_URI="/static/.*\.[a-f0-9]{12,}\.(css|js|png|jpg|jpeg|gif|ico|woff|ttf|otf|svg|scss|map|txt) 315360000"

# Deny invalid hosts before they get to Django (uncomment and change to your hostname(s)):
# ENV UWSGI_ROUTE_HOST="^(?!localhost:8000$) break:400"

# Change to a non-root user
USER ${APP_USER}:${APP_USER}

# Start uWSGI
CMD ["uwsgi", "--show-config"]
