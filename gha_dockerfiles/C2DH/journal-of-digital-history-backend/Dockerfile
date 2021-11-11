FROM python:3.8.0-alpine
WORKDIR /journal-of-digital-history-backend

ARG GIT_TAG
ARG GIT_BRANCH
ARG GIT_REVISION

RUN pip install --upgrade pip

RUN apk add --no-cache \
    postgresql-libs \
    libxml2 \
    libxslt \
# Pillow dependencies
    freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev \
    libxslt-dev

COPY jdh ./jdh
COPY jdhapi ./jdhapi
COPY jdhseo ./jdhseo
COPY jdhtasks ./jdhtasks
COPY dashboard ./dashboard
COPY schema ./schema
COPY dbconnection.py .
COPY manage.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apk del --no-cache .build-deps

RUN mkdir -p logs

ENV GIT_TAG=${GIT_TAG}
ENV GIT_BRANCH=${GIT_BRANCH}
ENV GIT_REVISION=${GIT_REVISION}

ENTRYPOINT python ./manage.py runserver
