############################################################
# Dockerfile to build Genropy container images
# Based on Ubuntu
############################################################

FROM genropy/genropy:latest
MAINTAINER Francesco Porcari - francesco@genropy.org

ADD . /home/genropy_projects/sandbox
EXPOSE 8080

ENV GNR_CURRENT_SITE sandbox
ENV GNR_WSGI_OPT_remote_edit t
RUN pip install psycopg2-binary
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD nginx.conf /home/nginx.conf
ADD mime.types /home/mime.types

ENTRYPOINT ["/usr/bin/supervisord"]

