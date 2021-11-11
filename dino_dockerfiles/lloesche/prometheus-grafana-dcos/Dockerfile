FROM grafana/grafana
MAINTAINER Lukas Loesche <lloesche@fedoraproject.org>

EXPOSE 3000

RUN apt-get update && \
    apt-get -y install python3-minimal python3-requests && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 /bin/dumb-init
ADD promdtsrcadd /bin/promdtsrcadd
ADD startup /bin/startup

RUN chmod +x /bin/promdtsrcadd /bin/startup /bin/dumb-init

ENTRYPOINT [ "/bin/dumb-init", "--" ]
CMD ["/bin/startup"]


