FROM python:alpine3.13

RUN apk add --no-cache --upgrade gcc musl-dev && \
    pip install --no-cache-dir --upgrade setuptools flexget==3.1.102 && \
    apk del --no-cache -r gcc musl-dev

COPY run.sh /

VOLUME ["/root/.flexget"]

EXPOSE 5050

CMD ["/run.sh" ]
