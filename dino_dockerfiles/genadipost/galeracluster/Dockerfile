FROM python:2.7
MAINTAINER Genadi Postrilko <genadipost@gmail.com>

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
            git \
            python-sphinx \
            texlive-latex-base \
            texlive-latex-extra \
            dvipng \
            apache2 \
    && pip install cloud-sptheme \
    && cd / \
    && git clone https://github.com/codership/documentation.git \
    && cd /documentation/galeracluster/ \
    && make dirhtml \
    && rm -rf /var/www/html \
    && ln -s /documentation/galeracluster/build/dirhtml /var/www/html

EXPOSE 80

CMD rm -f /usr/local/apache2/logs/httpd.pid && apachectl -DFOREGROUND
