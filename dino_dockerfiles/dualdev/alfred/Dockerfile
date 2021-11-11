FROM gliderlabs/alpine:3.6

RUN apk add --update python3 python3-dev libffi openssl libffi-dev build-base openssl-dev \
  && python3 -m ensurepip \
  && rm -r /usr/lib/python*/ensurepip \
  && pip3 install --upgrade pip setuptools \
  && if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi \
  && rm -r /root/.cache \
  && rm -rf /var/cache/apk/*

WORKDIR /tmp

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN apk del build-base libffi-dev build-base openssl-dev \
  && rm -rf /var/cache/apk/*

WORKDIR /app
COPY . /app