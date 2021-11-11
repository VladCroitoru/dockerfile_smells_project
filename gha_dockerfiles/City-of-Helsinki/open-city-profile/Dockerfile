# ==============================
FROM helsinkitest/python:3.7-slim as appbase
# ==============================

ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN mkdir /entrypoint

COPY --chown=appuser:appuser requirements*.txt /app/

RUN apt-install.sh \
    build-essential \
    libpq-dev \
    gdal-bin \
    netcat \
    pkg-config \
    python3-gdal \
    postgresql-client \
    && pip install -U pip \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && pip install --no-cache-dir -r /app/requirements-prod.txt \
    && apt-cleanup.sh build-essential pkg-config

COPY --chown=appuser:appuser docker-entrypoint.sh /entrypoint/docker-entrypoint.sh
ENTRYPOINT ["/entrypoint/docker-entrypoint.sh"]

# ==============================
FROM appbase as staticbuilder
# ==============================

ENV VAR_ROOT /app
COPY --chown=appuser:appuser . /app
RUN python manage.py collectstatic --noinput

# ==============================
FROM appbase as development
# ==============================

COPY --chown=appuser:appuser requirements-dev.txt /app/requirements-dev.txt
RUN pip install --no-cache-dir -r /app/requirements-dev.txt \
    && pip install --no-cache-dir pip-tools

ENV DEV_SERVER=1

COPY --chown=appuser:appuser . /app/

USER appuser

EXPOSE 8080/tcp

# ==============================
FROM appbase as production
# ==============================

COPY --from=staticbuilder --chown=appuser:appuser /app/static /app/static
COPY --chown=appuser:appuser . /app/

USER appuser

EXPOSE 8080/tcp
