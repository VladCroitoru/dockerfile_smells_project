FROM alpine

ENV AWS_REGION=us-east-1 LOG_FILE=/aws.conf LOG_GROUP=changeme

RUN apk update && \
    apk add --no-cache python curl && \
    curl https://bootstrap.pypa.io/get-pip.py -O && \
    python get-pip.py 'pip<7.0.0' --no-wheel && \
    mkdir /var/awslogs && mkdir /var/awslogs/state && mkdir /var/awslogs/etc &&  mkdir /var/awslogs/etc/config  && \
    pip install awscli-cwlogs && \
    pip uninstall setuptools pip -y && \
    apk --purge -v del curl && \
    rm -rf get-pip.py /var/cache/apk/* /root/.cache/* /usr/share/terminfo

ADD boot.sh /var/awslogs

ENTRYPOINT ["/bin/sh", "/var/awslogs/boot.sh"]