############################################################
# Dockerfile to build Genropy container images
# Based on Ubuntu
############################################################

FROM genropy/genropy
MAINTAINER Francesco Porcari - francesco@genropy.org

RUN pip install docker-py
RUN pip install sh
RUN pip install beautifulsoup4
ADD . /home/genropy_projects/dockereasy
EXPOSE 8990

ENV GNR_CURRENT_SITE dockereasy

ENTRYPOINT ["/usr/bin/supervisord"]

