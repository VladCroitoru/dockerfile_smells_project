FROM ubuntu:16.04

# Environment variables
ENV DOMAIN localhost
ENV USERNAME admin
ENV PASSWORD admin
ENV LC_CTYPE en_US.UTF-8
RUN locale-gen $LC_CTYPE

# Setup scripts for LibreOffice Online
ADD container-files /
RUN bash /install-libreoffice.sh

EXPOSE 9980

# Entry point
ENTRYPOINT ["/config/bootstrap.sh"]
CMD [""]

