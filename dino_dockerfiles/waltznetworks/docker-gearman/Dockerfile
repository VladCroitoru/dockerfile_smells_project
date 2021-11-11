FROM pataquets/gearmand

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y gearman-tools curl

# get ContainerPilot release
ENV CONTAINERPILOT_VERSION 2.4.1
RUN export CP_SHA1=198d96c8d7bfafb1ab6df96653c29701510b833c \
    && curl -Lso /tmp/containerpilot.tar.gz \
         "https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.tar.gz" \
    && echo "${CP_SHA1}  /tmp/containerpilot.tar.gz" | sha1sum -c \
    && tar zxf /tmp/containerpilot.tar.gz -C /bin \
    && rm /tmp/containerpilot.tar.gz

COPY containerpilot.json /etc

EXPOSE 4730

ENTRYPOINT ["/bin/containerpilot", "-config", "file://etc/containerpilot.json", "gearmand"]
