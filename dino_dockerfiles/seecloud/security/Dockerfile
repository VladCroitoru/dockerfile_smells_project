FROM debian:jessie

COPY . /app

RUN apt-get update \
    && apt-get install --yes --no-install-recommends --no-install-suggests \
        ca-certificates curl openssl python python-dev build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py \
    && python /tmp/get-pip.py \
    && pip install -r /app/requirements.txt \
    && pip install /app \
    && mkdir -p /opt/security \
    && cp -r /app/etc /app/entrypoint-all.sh /app/entrypoint-api.sh /opt/security/ \
    && rm -rf /app

WORKDIR /opt/security
EXPOSE 5000
