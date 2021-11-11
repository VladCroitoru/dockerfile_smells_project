FROM python:3.4.6-alpine

ENV ETCD_BASE /yoda
ENV DOCKER_URL http://172.17.42.1:4243
ENV ETCD_HOST 172.17.42.1
ENV ETCD_PORT 4001
ENV PROXY_HOST 172.17.42.1

ADD requirements.txt /opt/yoda-discover/requirements.txt
RUN apk add --no-cache --update --virtual build-dependencies \
          musl-dev \
          linux-headers \
          build-base \
          pcre-dev \
          libffi-dev \
          openssl-dev \

    # Python Dependencies
    && pip3 install --ignore-installed  --no-cache-dir  -r /opt/yoda-discover/requirements.txt \

    # Cleanup
    && apk del build-dependencies \
    && find /usr/local \
         \( -type d -a -name test -o -name tests \) -exec echo rm -rf '{}' + \
         -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec echo rm -f '{}' +


ADD . /opt/yoda-discover

WORKDIR /opt/yoda-discover
ENTRYPOINT ["/usr/local/bin/python3","-m"]
CMD ["discover.docker_poller"]
