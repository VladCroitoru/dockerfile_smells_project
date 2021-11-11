FROM alpine

RUN apk add --no-cache bash openssh-client rsync ansible git py2-pip \
    py2-yaml py2-paramiko py2-jinja2 py2-markupsafe py2-crypto \
    && pip2 install docker-compose s3cmd passlib \
    && apk del py2-pip
