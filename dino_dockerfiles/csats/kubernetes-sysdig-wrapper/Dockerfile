
FROM radial/busyboxplus:curl

RUN curl -o /usr/bin/docker https://get.docker.com/builds/Linux/x86_64/docker-1.8.3 && \
  chmod 755 /usr/bin/docker
WORKDIR /sysdig

ADD sysdig-wrapper /sysdig/sysdig-wrapper

CMD /sysdig/sysdig-wrapper
