ARG osversion=xenial
FROM ubuntu:${osversion}

ARG VERSION=master
ARG VCS_REF
ARG BUILD_DATE

RUN echo "VCS_REF: "${VCS_REF}", BUILD_DATE: "${BUILD_DATE}", VERSION: "${VERSION}

LABEL maintainer="frank.foerster@ime.fraunhofer.de" \
      description="Dockerfile providing the PROKKA annotation pipeline" \
      version=${VERSION} \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.vcs-url="https://github.com/greatfireball/ime_home.git"

RUN apt update && apt install --yes git python python-pip

WORKDIR /tmp
RUN git clone -b master https://github.com/ListerLab/HOME.git HOME

WORKDIR HOME

RUN pip install -r requirements.txt

RUN python setup.py install

VOLUME /data

WORKDIR /data


