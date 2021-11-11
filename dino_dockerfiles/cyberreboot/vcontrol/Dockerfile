FROM ubuntu:16.04
LABEL maintainer="Charlie Lewis <clewis@iqt.org>"

RUN apt-get update && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    iptables \
    iputils-ping \
    lxc \
    python-dev \
    python-pip \
    sshpass

# install docker
RUN curl -sSL https://get.docker.com/ | sh

# hacks for vmware driver
RUN curl -L https://github.com/vmware/govmomi/releases/download/v0.7.1/govc_linux_amd64.gz >govc.gz && gzip -d govc.gz && mv govc /usr/local/bin/govc
RUN chmod +x /usr/local/bin/govc

# install docker-machine
RUN curl -L https://github.com/docker/machine/releases/download/v0.8.2/docker-machine-`uname -s`-`uname -m` >/usr/local/bin/docker-machine && \
    chmod +x /usr/local/bin/docker-machine

# install vent
RUN curl -L https://github.com/CyberReboot/vent/releases/download/v0.3.1/vent.iso >boot2docker.iso && mkdir -p /root/.docker/machine/ && mv boot2docker.iso /root/.docker/machine/boot2docker.iso
RUN mkdir -p /root/.docker/machine/cache && ln -s /root/.docker/machine/boot2docker.iso /root/.docker/machine/cache/boot2docker.iso

# install vcontrol
ADD vcontrol/requirements.txt /vcontrol/requirements.txt
RUN pip install -r /vcontrol/requirements.txt
ADD . /vcontrol
RUN pip install -e /vcontrol

VOLUME /var/lib/docker
VOLUME /root/.docker
ENV PATH "$PATH":/vcontrol/bin
ENV VCONTROL_DAEMON http://localhost:8080
ENV VCONTROL_API_VERSION /v1
ENV VCONTROL_ENV docker
WORKDIR /vcontrol/bin

EXPOSE 8080

ENTRYPOINT ["vcontrol"]
CMD ["daemon"]
