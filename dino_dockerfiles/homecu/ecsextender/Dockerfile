FROM alpine:3.5

RUN apk update && \
    apk add curl groff less python2 py2-pip nmap git
RUN pip install awscli boto3 requests
RUN curl -sSL https://get.docker.com/builds/Linux/x86_64/docker-1.11.2.tgz > docker.tar.gz && \
    tar zxvf docker.tar.gz docker/docker && \
    mv docker/docker /usr/bin/ && \
    rm -rf docker.tar.gz docker

COPY run /
COPY overrides /overrides
COPY run.d /run.d

CMD /run
