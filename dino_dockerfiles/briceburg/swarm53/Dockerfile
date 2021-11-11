FROM alpine:3.6
RUN apk --no-cache add bash curl groff python py-pip &&\
  pip install --upgrade awscli==1.14.19 &&\
  apk --purge del py-pip

RUN curl -Lf https://download.docker.com/linux/static/stable/x86_64/docker-17.12.0-ce.tgz | \
      tar -xz -C /tmp &&\
    mv /tmp/docker/docker /usr/bin/ &&\
    rm -rf /tmp/docker

COPY src/swarm53.sh /usr/bin/swarm53
COPY src/topology-monitor.sh /usr/bin/swarm53-monitor
ENV PAGER="more"
ENTRYPOINT ["swarm53"]
