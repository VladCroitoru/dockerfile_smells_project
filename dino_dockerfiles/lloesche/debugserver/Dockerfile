FROM alpine

MAINTAINER Lukas Loesche "lloesche@fedoraproject.org"

ADD debugserver.py /
ADD requirements.txt /tmp/

RUN apk add --no-cache python3 libffi openssl \
        python3-dev libffi-dev openssl-dev build-base && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install -r /tmp/requirements.txt && \
    rm -r /root/.cache && \
    apk del python3-dev libffi-dev openssl-dev build-base

WORKDIR /
EXPOSE 80
ENTRYPOINT ["/debugserver.py"]
