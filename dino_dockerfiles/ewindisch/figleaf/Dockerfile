FROM ubuntu
MAINTAINER Eric Windisch <ewindisch@docker.com>

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9

RUN sh -c "echo deb http://get.docker.io/ubuntu docker main\
    > /etc/apt/sources.list.d/docker.list"

RUN apt-get update; \
    apt-get install -qqy lxc-docker python-pip apparmor \
                         socat; \
    apt-get clean
RUN pip install -U fig

RUN mkdir -p /opt/dind
COPY wrapdocker /opt/dind/
COPY docker-wrapper /opt/dind/
COPY run-fig /opt/dind/

RUN ln -s /opt/dind/docker-wrapper /opt/dind/docker
RUN ln -s /opt/dind/docker-wrapper /opt/dind/fig

# Add /opt/dind to PATH
ENV PATH /opt/dind:$PATH

RUN mkdir -p /opt/figapp

ONBUILD WORKDIR /opt/figapp
ONBUILD COPY fig.yml /opt/figapp/

COPY README.md /opt/dind/README.md
WORKDIR /opt/figapp
ENTRYPOINT ["/opt/dind/run-fig"]
