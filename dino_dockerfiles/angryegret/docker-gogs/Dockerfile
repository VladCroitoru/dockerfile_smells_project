FROM google/golang
# Based on https://github.com/codeskyblue/docker-gogs
MAINTAINER rgreget@gmail.com

# grab but do not build gogs
RUN git clone https://github.com/gogits/gogs.git /gopath/src/github.com/gogits/gogs

# set the working directory and add current stuff
WORKDIR /gopath/src/github.com/gogits/gogs
RUN git checkout master && \
    go get -v -tags "sqlite redis memecache" && \
    go build -tags "sqlite redis memecache" && \
    useradd --shell /bin/bash --system --comment gogits git

# prepare data
ENV GOGS_CUSTOM /data/gogs
RUN echo "export GOGS_CUSTOM=/data/gogs" >> /etc/profile

RUN apt-get update && \
    apt-get install -y rsync &&\
    apt-get upgrade -y && \
    apt-get clean -y && \
    apt-get autoclean -y && \
    apt-get autoremove -y && \
    rm -rf /usr/share/locale/* && \
    rm -rf /var/cache/debconf/*-old && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/share/doc/*
ADD . /gopath/src/github.com/gogits/gogs

EXPOSE 3000
ENTRYPOINT []
CMD ["./start.sh"]
