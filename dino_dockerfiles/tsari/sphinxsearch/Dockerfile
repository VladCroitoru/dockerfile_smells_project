FROM tsari/wheezy-apache-php
MAINTAINER Tibor Sári <tiborsari@gmx.de>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y

# install sphinx search and clean up to minimize the image size
RUN apt-get install -y \
    sphinxsearch \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD sphinx.conf /etc/sphinxsearch/sphinx.conf

VOLUME /home/root/sphinx

EXPOSE 5351 15351

ADD searchd.sh /bin/searchd.sh
RUN chmod +x /bin/searchd.sh

CMD ["searchd.sh"]