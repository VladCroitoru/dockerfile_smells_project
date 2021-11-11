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
COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps \
        make gcc libxml2-dev libxslt-dev git musl-dev \
    && apk add libxml2 libxslt \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir gunicorn \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-index --find-links=file:///deps -U articlemeta \
    && apk --purge del .build-deps \
    && rm requirements.txt \
    && rm -rf /deps

WORKDIR /app

ENV ARTICLEMETA_SETTINGS_FILE=/app/config.ini
ENV PYTHONUNBUFFERED 1

USER nobody

