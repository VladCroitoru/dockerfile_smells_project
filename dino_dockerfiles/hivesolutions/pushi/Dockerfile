FROM hivesolutions/python:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

EXPOSE 9090
EXPOSE 443

VOLUME /data

ENV LEVEL INFO
ENV APP_SERVER netius
ENV APP_SERVER_ENCODING gzip
ENV APP_HOST 0.0.0.0
ENV APP_PORT 9090
ENV APP_SSL 1
ENV APP_SSL_KEY /data/pushi.key
ENV APP_SSL_CER /data/pushi.cer
ENV SERVER_HOST=0.0.0.0
ENV SERVER_PORT=443
ENV SERVER_SSL 1
ENV SERVER_SSL_KEY /data/pushi.key
ENV SERVER_SSL_CER /data/pushi.cer
ENV MONGOHQ_URL mongodb://localhost
ENV FILE_LOG 1
ENV PUSHI_HANDLERS 1
ENV PYTHONPATH /src

ADD requirements.txt /
ADD extra.txt /
ADD src /src

RUN pip3 install -r /requirements.txt && pip3 install -r /extra.txt

CMD ["/usr/bin/python3", "/src/pushi/base/state.py"]
