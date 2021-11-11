FROM python:3.8-alpine

RUN apk add --no-cache --virtual .tmp-packeges build-base \
    && pip install dumb-init==1.2.5\
    && apk del .tmp-packeges

RUN apk add --no-cache git

RUN mkdir /app
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

RUN addgroup -S app && adduser -S -G app app
RUN chown -R app:app /app
USER app

COPY . /app/

WORKDIR /app
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]
CMD ["python3", "/app/main.py"]