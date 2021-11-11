FROM orctom/alpine:3.2
MAINTAINER Hao Chen <orctom@gmail.com>

RUN \
    apk add --update curl python-dev && rm -rf /var/cache/apk/* \
    && curl -L https://bootstrap.pypa.io/get-pip.py | python \
    && pip install flask

COPY . /docker-registry-ui

EXPOSE 8080
CMD ["/usr/bin/python", "/docker-registry-ui/app.py"]