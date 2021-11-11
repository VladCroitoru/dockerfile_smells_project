FROM python:3.9.6-slim

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN mkdir /artemis
RUN mkdir /static

WORKDIR /artemis

COPY ./requirements.txt /scripts/

RUN apt-get update && apt-get -y install \
    binutils \
    libproj-dev \
    gdal-bin \
    postgresql \
    postgresql-postgis \
    zlib1g \
    libstdc++6 \
    gcc \
    python3-dev \
    musl-dev \
    zlib1g-dev \
    libjpeg-dev \
    libpq-dev \
    g++ \
    libopenblas-dev \
    cmake

RUN apt-get autoclean && apt-get clean && apt-get autoremove

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /scripts/requirements.txt

RUN find -type d -name __pycache__ -prune -exec rm -rf {} \;

RUN rm -rf ~/.cache/pip
RUN rm -rf /scripts/