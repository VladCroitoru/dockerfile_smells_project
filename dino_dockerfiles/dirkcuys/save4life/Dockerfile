FROM ubuntu:14.04

MAINTAINER Dirk Uys <dirkcuys@gmail.com>

# Install requirements
RUN apt-get update && apt-get install -y \
    git-core \
    libpq-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    postgresql-client \
    python \
    python-dev \
    python-virtualenv \
    supervisor \
    redis-server

# Setup application
COPY requirements.txt /app/
RUN virtualenv /var/venv && /var/venv/bin/pip install -r /app/requirements.txt

COPY . /app/
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY config/docker-entry.sh /docker-entry.sh
RUN mkdir -p /var/lib/celery && useradd celery && chown celery:celery /var/lib/celery/

ENV DATABASE_URL="sqlite:////app/db.sqlite3"

EXPOSE 80

ENTRYPOINT ["/docker-entry.sh"]
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
