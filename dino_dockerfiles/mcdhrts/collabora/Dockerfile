FROM ubuntu:16.04

# Environment variables
ENV DOMAIN localhost
ENV USERNAME admin
ENV PASSWORD admin
ENV LC_CTYPE en_US.UTF-8

# Setup scripts for LibreOffice Online
ADD container-files /
RUN bash /install-libreoffice.sh
RUN chmod u+x /config/bootstrap.sh
# ADD ./elasticsearch.yml ${ES_PATH_CONF}/elasticsearch.yml

EXPOSE 9980

# Entry point
ENTRYPOINT ["/config/bootstrap.sh"]
CMD [""]

