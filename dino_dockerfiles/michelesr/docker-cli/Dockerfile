FROM debian:8

RUN apt update && apt install -y apt-transport-https

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \
      --recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \
    echo 'deb https://apt.dockerproject.org/repo debian-jessie main' \
      > /etc/apt/sources.list.d/docker.list && \
    apt update && apt install -y docker-engine
