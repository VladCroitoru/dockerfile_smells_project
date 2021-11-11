FROM ubuntu:16.04
MAINTAINER leafney "babycoolzx@126.com"

ENV GOGS_VERSION 0.11.29

RUN apt-get update && \
    set -x && \
    apt-get install -y git wget openssh-server tzdata && \
    groupadd git && useradd -d /home/git -m -g git git && \
    cd /tmp && \
    wget --no-check-certificate https://github.com/gogits/gogs/releases/download/v${GOGS_VERSION}/linux_amd64.tar.gz -O gogs.tar.gz && \
    tar -C /home/git -xzf gogs.tar.gz && \
    rm gogs.tar.gz && \
    ln -sf /usr/share/zoneinfo/Asia/ShangHai /etc/localtime && \
	echo "Asia/Shanghai" > /etc/timezone && \
	dpkg-reconfigure -f noninteractive tzdata && \
	wget --no-check-certificate -O /usr/local/bin/gosu https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 && \
	chmod +x /usr/local/bin/gosu && \
    rm -rf /var/lib/apt/lists/* /tmp/*

COPY ./run.sh /usr/local/bin/
COPY ./docker-entrypoint.sh /usr/local/bin/
RUN chmod +x usr/local/bin/docker-entrypoint.sh && \
    chmod +x usr/local/bin/run.sh
ENTRYPOINT ["docker-entrypoint.sh"]

# must set run directory to /home/git/gogs
WORKDIR /home/git/gogs
VOLUME ["/app"]

EXPOSE 22 3000

CMD ["run.sh"]