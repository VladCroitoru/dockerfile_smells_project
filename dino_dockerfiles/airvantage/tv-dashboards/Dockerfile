FROM python:2.7-alpine
MAINTAINER prieux@sierrawireless.com


# Install
RUN \
    pip install urllib3 python-dateutil pytz jira jinja2 tornado Flask requests && \
    addgroup -S engtv && \
    adduser -S -g engtv engtv && \
    mkdir -p /home/engtv/static/ && \
    mkdir -p /home/engtv/www
#

COPY static  /home/engtv/static
COPY www     /home/engtv/www

ADD scripts/engtv.sh /home/engtv/
ADD scripts/engtv.py /home/engtv/

USER engtv

EXPOSE 8080

ENTRYPOINT ["/home/engtv/engtv.sh"]
