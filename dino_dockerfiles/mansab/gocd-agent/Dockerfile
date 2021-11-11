FROM gocd/gocd-agent
MAINTAINER Mansab Uppal <mansab.uppal@gmail.com>

RUN apt-get update \
    && apt-get install -y apt-transport-https ca-certificates \
    && apt-key adv \
        --keyserver hkp://ha.pool.sks-keyservers.net:80 \
        --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

RUN echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" | \
    tee /etc/apt/sources.list.d/docker.list \
    && apt-get update

RUN apt-get install -y docker-engine \
    && update-rc.d docker defaults

RUN usermod -aG docker go

CMD /etc/init.d/docker start && /sbin/my_init
