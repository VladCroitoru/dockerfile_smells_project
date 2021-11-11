FROM python:2.7.11-alpine
MAINTAINER kubor <rkubo.4w@gmail.com>
LABEL name="dajalender" \
    vendor="kubor" \
    license="MIT" \
    build-date="2016-04-29"

RUN apk update && apk add git

RUN git clone https://github.com/kubor/dajalendar.git && \
    cd dajalendar && \
    python setup.py install

CMD dajalendar
