FROM python:3.5.2-alpine AS build
COPY . /src
RUN pip install --upgrade pip \
    && pip install wheel
RUN cd /src \
    && python setup.py bdist_wheel -d /deps


FROM python:3.5.2-alpine
MAINTAINER gustavo.fonseca@scielo.org

COPY --from=build /deps/* /deps/
COPY production.ini-TEMPLATE /app/config.ini
COPY alembic.ini-TEMPLATE /app/alembic.ini
COPY alembic /app/alembic/
COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps \
        make gcc libxml2-dev libxslt-dev git musl-dev postgresql-dev \
    && apk add libxml2 libxslt postgresql-libs \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-index --find-links=file:///deps -U doi_request \
    && apk --purge del .build-deps \
    && rm requirements.txt \
    && rm -rf /deps

WORKDIR /app

ENV PYTHONUNBUFFERED 1

USER nobody

