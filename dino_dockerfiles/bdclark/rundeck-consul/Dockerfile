FROM python:3-alpine

RUN apk add --no-cache \
    su-exec \
    tini

WORKDIR /app

COPY requirements.txt ./

RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
  && pip install -r requirements.txt \
  && apk del .build-deps

COPY app.py config.json start.sh ./

EXPOSE 8080

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["/app/start.sh"]
