FROM postgres:11.1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-plpython-$PG_MAJOR \
    && rm -rf /var/lib/apt/lists/*
