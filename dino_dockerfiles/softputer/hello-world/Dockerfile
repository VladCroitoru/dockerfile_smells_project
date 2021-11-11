FROM alpine:3.4
MAINTAINER JaysonGe <gyj3023@foxmail.com>

RUN apk add --update \
    python \
    python-dev \
    py-pip \
  && rm -rf /var/cache/apk/*

RUN pip install flake8

WORKDIR /app

EXPOSE 80

COPY . /app

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
