FROM alpine:3.3

ADD requirements.txt /crypto/requirements.txt

RUN apk update && apk upgrade \
  && apk add curl python3 \
  && curl -sS https://bootstrap.pypa.io/get-pip.py | python3

RUN apk add --no-cache --virtual=build-dependencies ca-certificates libffi-dev openssl-dev g++ make python3-dev \
  && pip3 install -r /crypto/requirements.txt \
  && apk del build-dependencies \
  && rm -rf /var/cache/apk/* \
  && rm -rf /root/.cache/pip/* \