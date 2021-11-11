FROM mysql:5.6

MAINTAINER Davi Marcondes Moreira <davi.marcondes.moreira@gmail.com>

ARG VCS_REF
ARG BUILD_DATE

LABEL org.label-schema.name="Docker/Magento-MySQL" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/devdrops/magento-mysql" \
      org.label-schema.schema-version="1.0"

COPY ./releases/* /releases/

RUN service mysql restart && \
    sleep 3 && \
    mysql -u root < /releases/1.7.0.2.sql
