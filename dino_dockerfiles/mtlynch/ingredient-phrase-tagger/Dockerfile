FROM mtlynch/crfpp
LABEL maintainer="Michael Lynch <michael@mtlynch.io>"

ARG BUILD_DATE
ENV VCS_URL https://github.com/mtlynch/ingredient-phrase-tagger.git
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="$VCS_URL" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1"

RUN apt-get update -y && \
    apt-get install -y git python3.9 python3-setuptools python3-pip && \
    rm -Rf /usr/share/doc && \
    rm -Rf /usr/share/man && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

ADD . /app
WORKDIR /app

RUN pip3 install .
