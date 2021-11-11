FROM python:2.7.11-alpine

RUN apk add --no-cache openssl ca-certificates

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENTRYPOINT [ "python", "./acmedns.py" ]