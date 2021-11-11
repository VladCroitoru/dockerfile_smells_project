FROM python:3.6-alpine3.13

RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add build-base && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

COPY ./app /app

ENTRYPOINT ["python"]

CMD ["main.py"]

