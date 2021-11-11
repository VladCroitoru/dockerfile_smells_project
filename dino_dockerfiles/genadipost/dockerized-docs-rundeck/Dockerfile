FROM httpd:2.4.23
MAINTAINER Genadi Postrilko <genadipost@gmail.com>

RUN apt-get -y update \
        && \
    apt-get -y install \
               make \
               groovy \
               pandoc \
               zip \
               git \
        && cd / \
        && git clone https://github.com/rundeck/rundeck \
        && cd /rundeck/docs \
        && make \
        && rm -rf /usr/local/apache2/htdocs \
        && ln -s /rundeck/docs/en/dist/html /usr/local/apache2/htdocs

