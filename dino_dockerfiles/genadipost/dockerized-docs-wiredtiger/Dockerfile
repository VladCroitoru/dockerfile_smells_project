FROM httpd:2.4.23-alpine
MAINTAINER Genadi Postrilko <genadipost@gmail.com>

RUN apk add --update \
            git \
        && cd / \
        && git clone https://github.com/wiredtiger/wiredtiger.github.com \
        && cd /wiredtiger.github.com \
        && rm -rf /usr/local/apache2/htdocs \
        && ln -s /wiredtiger.github.com /usr/local/apache2/htdocs

