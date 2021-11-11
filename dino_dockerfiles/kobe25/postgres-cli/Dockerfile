FROM debian:8
MAINTAINER Antonio Esposito "kobe@member.fsf.org"

RUN apt update && apt install -y \
  python-pip python-dev libpq-dev libevent-dev \
  postgresql-client osm2pgsql curl wget zip \
  && rm -rf /var/lib/apt/lists/*
RUN pip install pgcli

RUN useradd -u 1000 -d /tmp app
USER app

CMD ["true"]
