FROM ubuntu:14.04 

MAINTAINER Ron Kurr <kurr@kurron.org>

LABEL org.kurron.ide.name="Nomad" org.kurron.ide.version=0.4.0

ADD https://releases.hashicorp.com/nomad/0.4.0/nomad_0.4.0_linux_amd64.zip /tmp/ide.zip

RUN apt-get update && \
    apt-get install -y unzip ca-certificates && \
    unzip /tmp/ide.zip -d /usr/local/bin && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

RUN chmod 0555 /usr/local/bin/*

# So we can see any files that need to be evaluated
VOLUME ["/pwd"]

# We need to be able to communicate with the Docker engine
VOLUME ["/var/run/docker.sock"]

WORKDIR /pwd
ENTRYPOINT ["/usr/local/bin/nomad"]
CMD ["--version"]
#CMD ["agent", "-dev"]
