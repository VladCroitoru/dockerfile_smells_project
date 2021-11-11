FROM alpine:3.6

MAINTAINER Mateusz Adamek <mateusz.adamek@idemia.com>

WORKDIR /opt

RUN apk update \
    && apk add py-setuptools py-pip python-dev libffi-dev openssl-dev git gcc py-configobj linux-headers musl-dev \
    # install python deps
    && pip install --upgrade pip \
    && pip install PyYAML \
    && pip install six pbr \
    && pip install pyOpenSSL stevedore fasteners pyasn1 ndg-httpsclient ordereddict multi_key_dict sphinx sphinxcontrib-programoutput builders jenkins python-jenkins

RUN mkdir /opt/jenkins-job-builder
ADD . /opt/jenkins-job-builder

RUN cd /opt/jenkins-job-builder && python setup.py install

# clean all cache to clean space
RUN rm -fr /opt/jenkins-job-builder 

ENTRYPOINT ["/usr/bin/jenkins-jobs"]
