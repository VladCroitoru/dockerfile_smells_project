FROM gliderlabs/alpine:latest

RUN apk add --update \
    ca-certificates \
    openssl \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

WORKDIR /app

COPY requirements.txt /app
RUN virtualenv /env && /env/bin/pip install -r /app/requirements.txt
COPY . /app

CMD ["/env/bin/python", "system_monitor.py"]

