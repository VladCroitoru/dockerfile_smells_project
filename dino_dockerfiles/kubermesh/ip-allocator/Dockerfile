FROM python:3-alpine

COPY requirements.txt /app/

RUN apk --no-cache add --virtual build-dependencies gcc linux-headers musl-dev \
  && pip install -r /app/requirements.txt \
  && apk del build-dependencies

WORKDIR /app
COPY allocate.py /app

ENTRYPOINT ["/app/allocate.py"]
