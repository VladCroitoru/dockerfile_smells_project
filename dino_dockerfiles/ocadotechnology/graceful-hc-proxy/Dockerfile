FROM alpine:3.4

WORKDIR /

COPY graceful-hc-proxy.py /
COPY config.py            /
COPY requirements.txt     /

RUN set -xe; \
    apk update; \
    apk add py-pip gcc python-dev musl-dev; \
    pip install -r requirements.txt

USER guest
EXPOSE 8800

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8800", "-c", "/config.py"]
CMD ["-k", "gevent", "--access-logfile", "-", "graceful-hc-proxy:app"]

