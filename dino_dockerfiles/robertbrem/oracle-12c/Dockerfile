FROM centos:7
MAINTAINER Robert Brem <brem_robert@ĥotmail.com>

ADD assets /assets

RUN chmod -R 755 /assets
RUN /assets/setup.sh

EXPOSE 1521
EXPOSE 8080

CMD ["/assets/entrypoint.sh"]
