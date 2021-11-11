FROM debian:9

RUN apt update && apt install -y \
  python-pip \
  python-dev \
  libpq-dev \
  libevent-dev \
  postgresql-client-9.6 \
  osm2pgsql \
  curl \
  wget \
  zip \
  && rm -rf /var/lib/apt/lists/*
  
RUN pip install pgcli
RUN pip install psycopg2-binary

# Drop permissions and run as UID 1000 user
RUN adduser --disabled-login --disabled-password -u 1000 app

USER app

CMD ["true"]
