FROM python:2-alpine

MAINTAINER Akhyar Amarullah "akhyrul@gmail.com"

# Add the files
ADD root /

RUN apk upgrade --update && \
    apk add ca-certificates && \
    rm -rf /var/cache/apk/* && \
    pip install -r requirements.txt --upgrade && \
    addgroup python && \
    adduser -D -g "" -s /bin/sh -G python python

USER python
    
EXPOSE 5000/tcp
CMD ["python", "app.py"]
