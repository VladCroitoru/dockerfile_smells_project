FROM justbuchanan/docker-archlinux
MAINTAINER Justin Buchanan <justbuchanan@gmail.com>

RUN pacman -Syyu --noconfirm
RUN pacman -v -S --noconfirm go python python-numpy opencv hdf5 mencoder git

# clear package cache
RUN pacman -Scc --noconfirm

# West coast
# TODO: pull this from the host system?
# Borrowed from: https://serverfault.com/questions/683605/docker-container-time-timezone-will-not-reflect-changes
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV GOPATH=/go

ENV SRC_DIR=$GOPATH/src/github.com/justbuchanan/timelapse-server
RUN mkdir -p $SRC_DIR
WORKDIR $SRC_DIR

COPY image_brightness.py ./
COPY main.go ./
RUN go get ./...
RUN go build -o timelapse-server main.go

EXPOSE 8888
VOLUME /data
VOLUME /www
CMD ./timelapse-server --image-dir /data --out-dir /www 
