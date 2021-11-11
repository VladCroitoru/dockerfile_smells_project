FROM alpine:latest

RUN apk update && apk upgrade && apk add python py-pip py-setuptools git ca-certificates mysql-client mysql-client postgresql redis
RUN pip install python-dateutil python-magic
RUN git clone https://github.com/s3tools/s3cmd.git /opt/s3cmd
RUN ln -s /opt/s3cmd/s3cmd /usr/bin/s3cmd

ADD bin/ /app
