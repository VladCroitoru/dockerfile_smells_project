FROM httpd:2.4.23-alpine
MAINTAINER Genadi Postrilko <genadipost@gmail.com>

RUN apk add --update \
            make \
            python \
            py-pip \
            git \
            ruby \
        && pip install sphinx==1.2.3 \
        && cd / \
        && git clone https://github.com/chef/chef-web-docs \
        && cd /chef-web-docs \
        && make master \
        && rm -rf /usr/local/apache2/htdocs \
        && ln -s /chef-web-docs/build /usr/local/apache2/htdocs

