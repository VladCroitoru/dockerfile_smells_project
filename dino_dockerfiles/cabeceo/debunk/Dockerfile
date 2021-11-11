FROM debian:latest

RUN apt-get -qqy update && \
    apt-get install -y apt-utils debconf-utils && \
    echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.vendor="Cabeceo, LLC" \
      org.label-schema.url="http://cabeceo.co" \
      org.label-schema.name="debunk" \
      org.label-schema.description="debian latest w/ debconf-utils, apt-utils and non-interactive set" \    
      org.label-schema.version="v1.0.0" \
      org.label-schema.docker.schema-version="1.0" \
      org.label-schema.vcs-url="https://github.com/Cabeceo/debunk.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.build-date=$BUILD_DATE
