FROM python:3.8-alpine AS env

WORKDIR /server
COPY requirements.txt .
RUN set -x \
    && apk add --no-cache --upgrade -t build-deps build-base libffi-dev gcc musl-dev libc-dev \
    && python3 -m pip install --no-cache-dir -r ./requirements.txt \
    && apk del build-deps

FROM env AS production
COPY . .
CMD ["python3","./Server.py"]