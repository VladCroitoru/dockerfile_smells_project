FROM alpine:latest

RUN apk --update --no-cache add git iptables curl xz python py-pip procps


ADD  https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz /tmp

RUN tar -zxvf /tmp/docker-latest.tgz -C /tmp && mv /tmp/docker/* /bin \
&& rm -rf /tmp/docker*

RUN pip install docker-compose

EXPOSE 2375

ENTRYPOINT ["/bin/dockerd"]

CMD ["-H","tcp://0.0.0.0:2375"]
