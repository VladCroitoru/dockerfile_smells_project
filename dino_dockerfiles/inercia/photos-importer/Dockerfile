FROM python:2.7-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk update && \
    apk upgrade && \
    apk add git exiftool

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/
RUN pip install --no-cache-dir .

VOLUME ["/orig", "/dest"]
CMD    [ "photos_importer" ]
