FROM alpine:3.4

MAINTAINER Benjamin Pannell <admin@sierrasoftworks.com>

RUN set -ex \
    && apk --update add sudo \
    && apk --update add python py-pip openssl ca-certificates sshpass \
    && apk --update add --virtual build-dependencies python-dev libffi-dev openssl-dev build-base linux-headers musl-dev \
    && pip install --upgrade pip cffi \
    && pip install \
        "ansible" \
        "boto" \
        "dopy" \
        "six" \
        "azure>=0.7.1" \
        "cs>=0.6.10" \
        "docker-py>=1.7.0" \
        "pyrax" \
        "python-consul" \
        "requests" \
        "kazoo>=2.1" \
    && apk del build-dependencies \
    && rm -rf /var/cache/apk/* \
    && mkdir -p /etc/ansible \
    && echo 'localhost' > /etc/ansible/hosts

WORKDIR /ansible
VOLUME /ansible
ENV ANSIBLE_HOST_KEY_CHECKING=False

CMD ["ansible", "--version"]